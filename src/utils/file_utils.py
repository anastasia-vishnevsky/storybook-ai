from pathlib import Path
import uuid
from fastapi import UploadFile
import requests


def save_uploaded_file(file: UploadFile, upload_dir: str = "uploads") -> Path:
    """
    Saves an uploaded file to a specified directory and returns the file path.
    """
    Path(upload_dir).mkdir(parents=True, exist_ok=True)
    file_id = str(uuid.uuid4())
    file_path = Path(upload_dir) / f"{file_id}_{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return file_path


def save_image_from_url(url: str, save_dir: str = "generated/covers") -> str:
    """
    Downloads an image from a URL and saves it locally.
    """
    Path(save_dir).mkdir(parents=True, exist_ok=True)
    filename = f"{uuid.uuid4()}.png"
    file_path = Path(save_dir) / filename

    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, "wb") as f:
            f.write(response.content)
        return str(file_path)
    else:
        raise Exception(f"Failed to download image. Status code: {response.status_code}")


def save_story_to_file(story: str, save_dir: str = "generated/stories") -> str:
    """
    Saves the story to a .txt file and returns the path.
    """
    Path(save_dir).mkdir(parents=True, exist_ok=True)
    filename = f"{uuid.uuid4()}.txt"
    file_path = Path(save_dir) / filename

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(story.strip())

    return str(file_path)