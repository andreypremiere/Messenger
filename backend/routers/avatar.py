import io

from fastapi import APIRouter, UploadFile, File, Depends
from starlette.responses import StreamingResponse

from schemas.user import UserCredentials
from services.avatar_sevice import get_avatar_service, AvatarService
from utils.jwt_util import get_current_user

router = APIRouter()

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzQyYjAyNmYtNDAzOS00MjQzLWExNTQtODA3ZTVkZWM1YmEwIiwidW5pcXVlX25pY2tuYW1lIjoiYW5kcmV5X2RldiIsImRpc3BsYXllZF9uaWNrbmFtZSI6ImFuZHJleV9kZXYiLCJleHAiOjE3NTI3MjgzMzh9.Pcb53D_5vQAhqurzQX8_CLuo36PEcQpNCJaKPJ_2W6U


@router.post('/upload-avatar')
async def upload_avatar(file: UploadFile = File(...), user: UserCredentials = Depends(get_current_user),
                        avatar_service: AvatarService = Depends(get_avatar_service)):
    try:
        result = await avatar_service.upload_avatar(file.file, str(user.user_id))
    except Exception as e:
        print('Не удалось открыть изображение.', e)
        return None

    print("операция выполнена")

    return StreamingResponse(io.BytesIO(result), media_type=file.content_type)


@router.get('/get_user_photo_by_key/{key}')
async def get_photo_by_key(key: str, user: UserCredentials = Depends(get_current_user),
                           avatar_service: AvatarService = Depends(get_avatar_service)):
    result = await avatar_service.get_image_by_key(str(user.user_id), key)
    # print(result)

    if result is not None:
        return StreamingResponse(io.BytesIO(result), media_type='image/webp')
    else:
        return None


