from fastapi import Depends

from database import get_s3_client


class AvatarRepository:
    def __init__(self, s3):
        self.s3 = s3

    async def upload_image(self, images: dict):
        for key, image in images.items():
            await self.s3.put_object(
                Bucket='storage-avatars',
                Key=key,
                Body=image,
                ContentType='image/webp'
            )

    async def get_image_by_key(self, key: str) -> bytes | None:
        try:
            result = await self.s3.get_object(
                Bucket="storage-avatars",
                Key=key
            )
            data = await result["Body"].read()
            return data
        except Exception as e:
            print('Ошибка получения фото по ключу', e)
            return None


async def get_avatar_repository(s3=Depends(get_s3_client)):
    return AvatarRepository(s3)
