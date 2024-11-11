from src.models.document_word import DocumentWord
from src.utils.repository import SQLAlchemyRepository


class DocumentWordRepository(SQLAlchemyRepository):
    """
    Repository class for License model.

    Inherits from:
        SQLAlchemyRepository: Base class for SQLAlchemy operations.

    Attributes:
        model: The SQLAlchemy model class associated with this repository.
    """
    model = DocumentWord
