import strawberry


@strawberry.type
class Seller:
    id: str
    tags: str
