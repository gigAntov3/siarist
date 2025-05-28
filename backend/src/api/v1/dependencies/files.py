from services.files import FilesService
from repositories.files import FilesRepository


def files_service():
    return FilesService(FilesRepository)