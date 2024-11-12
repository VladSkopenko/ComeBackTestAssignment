from io import BytesIO

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi.params import File
from fastapi.responses import StreamingResponse
from fastapi import status

from src.core.logging_config import get_logger
from src.routers.dependencies import DocumentWordServiceDep
from src.routers.dependencies import UOWDep
from src.schemas.document_word import DocumentWordSchema
from src.services.drop_box_service import DropboxService

logger = get_logger(__name__)
dropbox_service = DropboxService()

router = APIRouter(
    prefix="/document_word",
    tags=["Documents Word"],
)


@router.post("/upload", response_model=DocumentWordSchema, status_code=status.HTTP_201_CREATED)
async def upload_to_dropbox(
        document_service: DocumentWordServiceDep,
        uow: UOWDep,
        file: UploadFile = File(...),
):
    dropbox_path = f"/{file.filename}"
    await dropbox_service.upload_file(file, dropbox_path=dropbox_path)
    document_new = await document_service.create_document_word(uow, dropbox_path)
    return document_new


@router.get("/download/{file_name}")
async def download_document(file_name: str):
    dropbox_path = f"/{file_name}"
    file_name, file_content = dropbox_service.download_file(dropbox_path)
    if file_content:
        return StreamingResponse(BytesIO(file_content), media_type="application/octet-stream",
                                 headers={"Content-Disposition": f"attachment; filename={file_name}"})
