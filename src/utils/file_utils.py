from pathlib import Path
import uuid
from fastapi import UploadFile


def save_uploaded_file(file: UploadFile, upload_dir: str = "uploads") -> Path:
    """
    Saves an uploaded file to a specified directory and returns the file path.

    Args:
        file (UploadFile): Uploaded file object from FastAPI.
        upload_dir (str): Directory to save the file. Default is 'uploads'.

    Returns:
        Path: Full path to the saved file.
    """
    Path(upload_dir).mkdir(parents=True, exist_ok=True)
    file_id = str(uuid.uuid4())
    file_path = Path(upload_dir) / f"{file_id}_{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return file_path
