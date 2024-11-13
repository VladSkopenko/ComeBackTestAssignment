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
from src.services.jap_formatted import JapFormatter
from src.utils.extract_data import extract_data_from_docx

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


@router.patch("/format/{document_id}", status_code=status.HTTP_200_OK, response_model=DocumentWordSchema)
async def format_document(
        document_id: int,
        document_service: DocumentWordServiceDep,
        uow: UOWDep,
):
    document = await document_service.get_document_word_by_id(uow, document_id)
    dropbox_path = document.original_document
    file_name, file_content = dropbox_service.open_file_from_dropbox(dropbox_path)
    document_data = extract_data_from_docx(file_content)
    formatter = JapFormatter(
        title=document_data["title"],
        authors=document_data["authors"],
        affiliations=document_data["affiliations"],
        abstract=document_data["abstract"],
        keywords=document_data["keywords"],
        main_text=document_data["main_text"],
        references=document_data["references"]
    )
    formatter.format_title_page()
    formatter.format_abstract()
    formatter.format_keywords()
    formatter.format_main_text()
    formatter.format_references()
    formatted_doc = formatter.doc
    docx_stream = BytesIO()
    formatted_doc.save(docx_stream)
    docx_stream.seek(0)
    new_dropbox_path = f"/formatted_apa_{file_name}"
    document_updated = await document_service.update_document_word_by_id(uow, document_id, new_dropbox_path)
    dropbox_service.upload_with_overwrite(docx_stream, dropbox_path=new_dropbox_path)
    return document_updated



