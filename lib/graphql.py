import strawberry

from lib.models.inputs.create_user_otp_input import CreateUserOtpInput
from lib.models.inputs.create_user_input import CreateUserInput
from lib.models.types.user import User


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        pass


@strawberry.type
class Mutation:
    @strawberry.field
    def create_user(self, user: CreateUserInput) -> User:
        pass

    @strawberry.field
    def create_user_otp(self, user: CreateUserOtpInput) -> bool:
        pass
