from fastapi import FastAPI, UploadFile, File
from src.utils.file_utils import save_uploaded_file
from src.utils.image_captioner import get_image_caption
from src.services.story_generator import generate_story
from src.services.cover_generator import generate_cover
from src.schemas import StorybookResponse
from src.utils.logger import logger

# Create FastAPI app instance
app = FastAPI(
    title="Storybook Generator API",
    description="Generates stories and covers based on uploaded images"
)

@app.get("/")
def read_root():
    return {"message": "Storybook API is running!"}

@app.post("/generate-storybook", response_model=StorybookResponse)
async def generate_storybook(file: UploadFile = File(...)):

    # Save uploaded file to uploads/ folder with a unique name
    file_path = save_uploaded_file(file)
    logger.info(f"Uploaded file saved to: {file_path}")

    # Generate caption using BLIP model
    caption = get_image_caption(str(file_path))
    logger.info(f"Generated image caption: {caption}")

    # Generate story using GPT
    story = generate_story(caption)
    logger.info(f"Generated story: {story.strip().replace(chr(10), ' ')}")

    # Generate cover image using DALL·E
    cover_url = generate_cover(caption)
    logger.info(f"Cover image URL: {cover_url}")

    # Return the storybook response
    return {
        "caption": caption,
        "story": story,
        "cover_url": cover_url
    }
