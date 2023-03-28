from typing import Optional

import strawberry

from lib.models.types.seller import Seller


@strawberry.type
class User:
    id: str
    image_url: Optional[str]
    email: str
    password: Optional[str]
    googleIdToken: Optional[str]
    facebookAccessToken: Optional[str]
    phone_number: str
    seller: Optional[Seller]
