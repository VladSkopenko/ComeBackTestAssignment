from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict


class DocumentWordSchema(BaseModel):
    """
    Schema for the license ID.
    """

    id: UUID

    model_config = ConfigDict(from_attributes=True)
