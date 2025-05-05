from openai import OpenAI
from src.config import settings
from src.prompts import build_dalle_prompt

# Set up OpenAI client
client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_cover(caption: str) -> str:
    """
    Generates an image URL using DALL·E 3 based on the caption.

    Args:
        caption (str): Description for the image generation.

    Returns:
        str: URL of the generated image.
    """
    formatted_prompt = build_dalle_prompt(caption)

    response = client.images.generate(
        model=settings.DALLE_MODEL,
        prompt=formatted_prompt,
        size="1024x1024",
        n=1
    )

    image_url = response.data[0].url
    return image_url