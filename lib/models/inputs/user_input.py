from typing import Optional

import strawberry


@strawberry.input
class UserInput:
    email: Optional[str]
    password: Optional[str]
    googleIdToken: Optional[str]
    facebookAccessToken: Optional[str]
    otp: Optional[str]
