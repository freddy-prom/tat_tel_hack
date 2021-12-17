from typing import List, Optional

from pydantic import AnyHttpUrl, BaseModel, Field

from .base_request_schema import BaseRequestSchema


class AddGoodRequestSchema(BaseRequestSchema):
    class BodySchema(BaseModel):
        name: str = Field(min_length=1, max_length=255)
        description: str
        image: str
        price: int
        active: bool
        count: int

    body: BodySchema
