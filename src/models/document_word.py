from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.models.base import Base


class DocumentWord(Base):
    __tablename__ = "documents_word"

    id: Mapped[int] = mapped_column(primary_key=True)
    original_document: Mapped[str] = mapped_column(String, nullable=False)
    formatted_apa: Mapped[str] = mapped_column(String, nullable=True)
    formatted_something_else: Mapped[str] = mapped_column(String, nullable=True)
