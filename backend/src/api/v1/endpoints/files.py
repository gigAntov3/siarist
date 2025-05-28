from typing import Annotated

from services.files import FilesService

from fastapi import APIRouter, File, UploadFile, Depends

from api.v1.dependencies.files import files_service

from schemas.files import FileSchema, AnswerFileSchema


router = APIRouter(
    prefix="/files",
    tags=["Files"],
)


@router.post("/upload")
async def upload_file(
    files_service: Annotated[FilesService, Depends(files_service)],
    file: UploadFile = File(...)
) -> AnswerFileSchema:      
    file: FileSchema = await files_service.upload_file(file)
    return AnswerFileSchema(ok=True, message="File uploaded successfully", file=file)