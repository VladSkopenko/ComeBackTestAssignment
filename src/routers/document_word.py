from fastapi import APIRouter
from fastapi import status
from starlette.requests import Request

from src.core.logging_config import get_logger

logger = get_logger(__name__)

router = APIRouter(
    prefix="/document_word",
    tags=["Documents Word"],
)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_main_page(request: Request):
    return {"message": "Hello World"}
