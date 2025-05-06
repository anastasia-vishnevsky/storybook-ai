from fastapi import FastAPI, UploadFile, File
from src.utils.file_utils import save_uploaded_file, save_image_from_url, save_story_to_file
from src.utils.image_captioner import get_image_caption
from src.services.story_generator import generate_story
from src.services.cover_generator import generate_cover
from src.schemas import StorybookResponse
from src.utils.logger import logger

app = FastAPI(
    title="Storybook Generator API",
    description="Generates stories and covers based on uploaded images"
)

@app.get("/")
def read_root():
    return {"message": "Storybook API is running!"}

@app.post("/generate-storybook", response_model=StorybookResponse)
async def generate_storybook(file: UploadFile = File(...)):
    # Save uploaded image and get file_id
    file_id, file_path = save_uploaded_file(file)
    logger.info(f"Uploaded file saved to: {file_path}")

    # Generate caption using BLIP
    caption = get_image_caption(str(file_path))
    logger.info(f"Generated image caption: {caption}")

    # Generate story using GPT
    story = generate_story(caption)
    logger.info(f"Generated story: {story.strip().replace(chr(10), ' ')}")

    # Generate cover using DALL·E
    cover_url = generate_cover(caption)
    logger.info(f"Cover image URL: {cover_url}")

    # Save generated content
    saved_cover_path = save_image_from_url(file_id, cover_url)
    saved_story_path = save_story_to_file(file_id, story)
    logger.info(f"Saved cover to: {saved_cover_path}")
    logger.info(f"Saved story to: {saved_story_path}")

    # Return the storybook response
    return {
        "caption": caption,
        "story": story,
        "cover_url": cover_url
    }