import uuid
from fastapi import UploadFile

from utils.repository import BaseRepository

from schemas.files import FileSchema


class FilesService:

    def __init__(self, files_repo: BaseRepository):
        self.files_repo = files_repo()

    def _get_filename(self, file: UploadFile):
        return f"{uuid.uuid4()}.{file.filename.split('.')[-1]}"

    async def upload_file(self, file: UploadFile):
        file_name = self._get_filename(file)
        await self.files_repo.upload_file(file_name, await file.read())
        url = await self.files_repo.generate_presigned_url(file_name)
        return FileSchema(file_name=file_name, url=url)
