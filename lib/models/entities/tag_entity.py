from beanie import Document


class TagEntity(Document):
    id: str
    label: str
