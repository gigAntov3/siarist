import os
import asyncio
import aiohttp
from bot.services.api.schemas.files import AnswerFileAdd, File

class FilesAPI:
    BASE_URL = "http://127.0.0.1:8000/files/upload"

    async def upload_file(self, file_path: str) -> File:
        url = f"http://127.0.0.1:8000/files/upload"

        form = aiohttp.FormData()
        file_name = os.path.basename(file_path)

        # Открываем файл и добавляем его в форму
        with open(file_path, 'rb') as f:
            form.add_field(
                name='file',
                value=f,
                filename=file_name,
                content_type='application/octet-stream'
            )

            async with aiohttp.ClientSession() as session:
                async with session.post(url, data=form) as response:
                    response_data = await response.json()
                    return AnswerFileAdd(**response_data).file



if __name__ == "__main__":
    api = FilesAPI()
    asyncio.run(api.upload_file("asdasd"))
