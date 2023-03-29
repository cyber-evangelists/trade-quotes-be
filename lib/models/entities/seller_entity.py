from typing import List, Optional

from beanie import Document, Link

from lib.models.entities.tag_entity import TagEntity


class SellerEntity(Document):
    business_name: Optional[str]
    post_code: Optional[str]
    tags: Optional[List[Link[TagEntity]]]
