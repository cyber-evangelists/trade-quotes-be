from typing import List

from beanie import Document

from lib.models.entities.tag_entity import TagEntity


class SellerEntity(Document):
    tags: List[TagEntity]
