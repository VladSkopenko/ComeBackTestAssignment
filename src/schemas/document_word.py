from datetime import datetime
from uuid import UUID
from typing import Optional
from pydantic import BaseModel
from pydantic import ConfigDict


class DocumentWordSchema(BaseModel):
    """
    Schema for the document word model.
    """

    id: int
    formatted_draft: Optional[str]
    formatted_apa:  Optional[str]
    formatted_something_else:  Optional[str]
    original_document: str
    updated_at: datetime
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
