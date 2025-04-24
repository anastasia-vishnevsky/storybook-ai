import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_cover(prompt: str) -> str:
    """
    Generates an image URL using DALL·E 2 based on the prompt.
    Args:
        prompt (str): Description for the image generation.
    Returns:
        str: URL of the generated image.
    """

    formatted_prompt = (
        f"Create an illustration in the style of a children's storybook cover, featuring: {prompt}"
    )

    response = client.images.generate(
        model="dall-e-3",
        prompt=formatted_prompt,
        size="1024x1024",
        n=1
    )

    image_url = response.data[0].url
    return image_url
