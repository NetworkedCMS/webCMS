import logging
import os
import os.path
from uuid import uuid4
import aiofiles
from PIL import Image
from aiobotocore.session import get_session
from networkedcms.settings.conf import settings
from werkzeug.datastructures import FileStorage
from networkedcms.errors.files import FileExtNotAllowed, FileMaxSizeLimit, NoSuchFieldFound

logger = logging.getLogger(__name__)

ALLOWED_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif'}


class FileUpload:
    def __init__(
            self,
            max_size: int = 1024 ** 5
    ):
        self.max_size = max_size
        self.allow_extensions = ALLOWED_EXTENSIONS
        self.uploads_dir = settings.IMAGE_UPLOAD_PATH

    async def save_file(self, filename):
        file_path = os.path.join(self.uploads_dir, filename)
        session = get_session()
        async with aiofiles.open(file_path, "rb") as f:
            """async with session.create_client(self.service, aws_access_key_id=self.aws_access_key_id,
                aws_secret_access_key=self.aws_secret_access_key) as client:
                file_upload_response = await client.put_object(ACL="public-read", Bucket='networkedstorage', Key=f'networked/{filename}', Body=await f.read())
                if file_upload_response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                    logger.info(f"https://networkedstorage.s3.eu-west-2.amazonaws.com/networked/{filename}")
                    return {'url': f'https://networkedstorage.s3.eu-west-2.amazonaws.com/networked/{filename}', 'filename':filename}
                else:
                    raise HTTPException(status_code=400, detail="Failed to upload in S3")"""
            pass

    async def compress(self, source_file, destination_filename: str):
        try:
            img = Image.open(source_file)
            if img.mode in ("RGBA", "P"):
                img_conv = img.convert('RGB')
                img_conv.save(os.path.join(self.uploads_dir,
                              destination_filename), optimize=True, quality=65)
                img_conv.close()
            else:
                img.save(os.path.join(self.uploads_dir,
                         destination_filename), optimize=True, quality=65)
                img.close()
            print(img)
            return await self.save_file(destination_filename)
        except Exception as e:
            raise HTTPException(detail="Could not process one or more images, try selecting a different image",
                                status_code=500)

    async def pass_file(self, file: FileStorage):
        filename = file.filename
        content = file.stream
        file_size = len(content)
        if file_size > self.max_size:
            raise FileMaxSizeLimit(
                f"File size {file_size} exceeds max size {self.max_size}")
        if self.allow_extensions:
            source_extension = os.path.splitext(filename)[1]
            if not source_extension in self.allow_extensions:
                raise FileExtNotAllowed(
                    f"File ext {source_extension} is not allowed of {self.allow_extensions}"
                )
            destination_filename = uuid4().hex + source_extension
        return await self.compress(destination_filename=destination_filename, source_file=file.file)
