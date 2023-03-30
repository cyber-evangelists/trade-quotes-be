from typing import Optional

import bcrypt
import strawberry

from lib.models.entities.seller_tag_entity import SellerTagEntity
from lib.models.entities.user_entity import UserEntity
from lib.models.inputs.create_user_otp_input import CreateUserOtpInput
from lib.models.inputs.create_user_input import CreateUserInput
from lib.models.inputs.seller_tag_input import SellerTagInput
from lib.models.inputs.user_input import UserInput
from lib.models.types.tag import Tag
from lib.models.types.tag_page import TagPage
from lib.models.types.user import User
from lib.services import bcrypt
from lib.utils import user_util


@strawberry.type
class Query:
    @strawberry.field
    async def user(self, user: UserInput) -> User:
        if user.email and user.password:
            searched_user = await UserEntity.find_one(UserEntity.email == user.email)
            if bcrypt.check(user.password, searched_user.password):
                return user_util.user_entity_to_user(searched_user)

        raise Exception('Insufficient credentials')

    @strawberry.field
    async def sellerTags(self, tags: Optional[SellerTagInput] = None) -> TagPage:
        total = await SellerTagEntity.count()
        if tags.search:
            return TagPage(
                items=[Tag(id=t.id, label=t.label) for t in await SellerTagEntity.find(
                    {'label': {'$regex': f'^{tags.search}.*$', '$options': 'i'}}).to_list()],
                page=1,
                total=total,
            )

        return TagPage(
            items=[Tag(id=t.id, label=t.label)
                   for t in await SellerTagEntity.find_all().to_list()],
            page=1,
            total=total,
        )


@strawberry.type
class Mutation:
    @strawberry.field
    async def create_user(self, user: CreateUserInput) -> User:
        if not (user.password or user.google_id_token or user.facebook_access_token):
            raise Exception(
                'One of password, googleIdToken or facebookAccessToken must be provided')

        user_entity = UserEntity(
            email=user.email,
            phone_number=user.phone_number,
            password=bcrypt.hash(user.password),
            google_id_token=user.google_id_token,
            facebook_access_token=user.facebook_access_token,
        )
        await user_entity.save()
        inserted_user = await UserEntity.find_one(UserEntity.email == user.email)
        return user_util.user_entity_to_user(inserted_user)

    @strawberry.field
    def create_user_otp(self, user: CreateUserOtpInput) -> bool:
        pass
