from pydantic import BaseModel


class ImageUrl(BaseModel):
    image_url: str


class Avatar(BaseModel):
    url_bib_image: ImageUrl
    url_norm_image: ImageUrl
    url_small_image: ImageUrl


class UserPhotos:
    user_id: str
    avatar: Avatar
    photos: [ImageUrl]
