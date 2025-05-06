from pathlib import Path
import uuid
from fastapi import UploadFile
import requests
from datetime import datetime


def generate_file_id() -> str:
    """
    Generates a unique file ID based on timestamp and short UUID for grouping.
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    short_uuid = uuid.uuid4().hex[:8]
    return f"{timestamp}_{short_uuid}"


def save_uploaded_file(file: UploadFile, upload_dir: str = "uploads") -> tuple[str, Path]:
    """
    Saves an uploaded file with a shared file ID and returns the ID and path.
    """
    Path(upload_dir).mkdir(parents=True, exist_ok=True)
    file_id = generate_file_id()
    ext = Path(file.filename).suffix or ".jpg"
    file_path = Path(upload_dir) / f"{file_id}_uploaded{ext}"

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return file_id, file_path


def save_image_from_url(file_id: str, url: str, save_dir: str = "generated/covers") -> str:
    """
    Downloads and saves a generated image using the shared file ID.
    """
    Path(save_dir).mkdir(parents=True, exist_ok=True)
    file_path = Path(save_dir) / f"{file_id}_cover.png"

    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, "wb") as f:
            f.write(response.content)
        return str(file_path)
    else:
        raise Exception(f"Failed to download image. Status code: {response.status_code}")


def save_story_to_file(file_id: str, story: str, save_dir: str = "generated/stories") -> str:
    """
    Saves a story using the shared file ID.
    """
    Path(save_dir).mkdir(parents=True, exist_ok=True)
    file_path = Path(save_dir) / f"{file_id}_story.txt"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(story.strip())

    return str(file_path)