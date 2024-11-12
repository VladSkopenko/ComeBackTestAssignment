import os
from io import BytesIO

import dropbox
from dropbox.files import WriteMode
from fastapi import UploadFile

from src.core.config import settings


class DropboxService:
    def __init__(self):
        self.access_token = settings.dropbox.token
        self.dbx = dropbox.Dropbox(self.access_token)

    async def upload_file(self, file: UploadFile, dropbox_path: str):
        file_content = await file.read()
        self.dbx.files_upload(file_content, dropbox_path)

    def upload_file2(self, file: BytesIO, dropbox_path: str):
        file_content = file.read()
        self.dbx.files_upload(file_content, dropbox_path, mode=WriteMode('overwrite'))

    def download_file(self, dropbox_path: str):
        metadata, response = self.dbx.files_download(dropbox_path)
        return metadata.name, response.content

    def open_file_from_dropbox(self, dropbox_path: str):
        """
        Открывает файл из Dropbox и возвращает его содержимое в памяти.

        :param dropbox_path: Путь к файлу на Dropbox.
        :return: Имя файла и его содержимое в байтах.
        """
        metadata, response = self.dbx.files_download(dropbox_path)
        return metadata.name, response.content
