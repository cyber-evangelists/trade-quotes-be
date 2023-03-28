from typing import Optional

from beanie import Document, Indexed

from lib.models.entities.seller_entity import SellerEntity


class UserEntity(Document):
    image_url: Optional[str] = None
    email: Indexed(str, unique=True)
    password: Optional[str] = None
    google_id_token: Optional[str] = None
    facebook_access_token: Optional[str] = None
    phone_number: str
    seller: Optional[SellerEntity] = None
