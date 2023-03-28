from typing import Optional

from beanie import Document

from lib.models.entities.seller_entity import SellerEntity


class UserEntity(Document):
    id: str
    image_url: Optional[str]
    email: str
    password: Optional[str]
    googleIdToken: Optional[str]
    facebookAccessToken: Optional[str]
    phone_number: str
    seller: Optional[SellerEntity]
