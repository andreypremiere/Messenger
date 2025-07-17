import io
from typing import BinaryIO

from PIL import Image
from fastapi import Depends

from repositories.avatar_repository import get_avatar_repository, AvatarRepository


class AvatarService:
    def __init__(self, avatar_repo: AvatarRepository):
        self.avatar_repo = avatar_repo
        self.SIZE_NORM = 500
        self.SIZE_USUAL = 64
        self.SIZE_SMALL = 32

    async def to_bytes(self, pil_img):
        output = io.BytesIO()
        pil_img.save(output, format="JPEG", quality=100)
        output.seek(0)
        return output.read()

    async def upload_avatar(self, image: BinaryIO, user_id: str):
        with Image.open(image) as img:
            width, height = img.size

            if width < self.SIZE_NORM or height < self.SIZE_NORM:
                return None
            else:
                print('Размер изображения не соответствует требуемому')

            center_image = (width/2, height/2)

            min_size = min(width, height)

            if width == min_size:
                # (left, upper, right, lower)
                img = img.crop((0, center_image[1] - center_image[0],
                                         min_size, center_image[1] + center_image[0]))
            else:
                img = img.crop((center_image[0] - center_image[1], 0,
                                         center_image[0] + center_image[1], min_size))

            cropped_image = img.resize((self.SIZE_NORM, self.SIZE_NORM))
            print('Размер нормального изображения:', cropped_image.size)

            usual_image = img.resize((self.SIZE_USUAL, self.SIZE_USUAL))
            print('Размер обычного изображения:', usual_image.size)

            small_image = img.resize((self.SIZE_SMALL, self.SIZE_SMALL))
            print('Размер маленького изображения:', small_image.size)

        big_image = await self.to_bytes(cropped_image)
        norm_image = await self.to_bytes(usual_image)
        small_image = await self.to_bytes(small_image)

        result = None

        images = {
            f'{user_id}_big': big_image,
            f'{user_id}_norm': norm_image,
            f'{user_id}_small': small_image
        }

        try:
            await self.avatar_repo.upload_image(images)
            return big_image
        except Exception as e:
            print('Ошибка добавления аватарок в хранилище', e)
            return None

    async def get_image_by_key(self, user_id: str, key: str) -> bytes | None:
        key = f'{user_id}_{key}'
        return await self.avatar_repo.get_image_by_key(key)


async def get_avatar_service(avatar_repo: AvatarRepository = Depends(get_avatar_repository)):
    return AvatarService(avatar_repo)
