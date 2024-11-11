from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )


class DocumentWord(Base):
    __tablename__ = "documents_word"

    id: Mapped[int] = mapped_column(primary_key=True)
    original_document: Mapped[str] = mapped_column(String, nullable=False)
    formatted_apa: Mapped[str] = mapped_column(String, nullable=True)
    formatted_something_else: Mapped[str] = mapped_column(String, nullable=True)
