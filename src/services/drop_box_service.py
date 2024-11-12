import os

import dropbox
from fastapi import UploadFile

from src.core.config import settings


class DropboxService:
    def __init__(self):
        self.access_token = settings.dropbox.token
        self.dbx = dropbox.Dropbox(self.access_token)

    async def upload_file(self, file: UploadFile, dropbox_path: str):
        file_content = await file.read()
        self.dbx.files_upload(file_content, dropbox_path)

    def download_file(self, dropbox_path: str):
        metadata, response = self.dbx.files_download(dropbox_path)
        return metadata.name, response.content

