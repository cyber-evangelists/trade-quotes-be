from typing import List, Optional

import strawberry

from lib.models.inputs.create_user_seller_input import CreateUserSellerInput


@strawberry.input
class CreateUserInput:
    email: str
    password: Optional[str]
    googleIdToken: Optional[str]
    facebookAccessToken: Optional[str]
    phone_number: str
    seller: Optional[CreateUserSellerInput]
