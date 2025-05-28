import asyncio
from utils.s3 import create_s3_session

class FilesRepository():
    BUCKET_NAME = 'mindsocial'

    def __init__(self):
        self.s3 = create_s3_session()  # уже готовый клиент, не session

    async def upload_file(self, file_name: str, file_data: bytes):
        print(file_name)
        await asyncio.to_thread(
            self.s3.put_object,
            Bucket=self.BUCKET_NAME,
            Key=file_name,
            Body=file_data
        )

    async def generate_presigned_url(self, file_name: str, expiration: int = 3600):
        return await asyncio.to_thread(
            self.s3.generate_presigned_url,
            ClientMethod='get_object',
            Params={'Bucket': self.BUCKET_NAME, 'Key': file_name},
            ExpiresIn=expiration
        )
