import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    # OpenAI API key
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # FastAPI host and port (used in run.py)
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", "8000"))

    # Base URL for internal services or Streamlit
    BASE_URL = os.getenv("BASE_URL", f"http://{HOST}:{PORT}")

    # External API URL for Streamlit
    API_URL = os.getenv("API_URL", BASE_URL)

    # Docker detection
    IN_DOCKER = os.getenv("IN_DOCKER") == "1"

    # If in Docker, replace localhost with container name
    if IN_DOCKER:
        API_URL = API_URL.replace("localhost", "storybook-api")

    # Model names
    BLIP_MODEL = os.getenv("BLIP_MODEL", "Salesforce/blip-image-captioning-base")
    GPT_MODEL = os.getenv("GPT_MODEL", "gpt-4o-mini")
    DALLE_MODEL = os.getenv("DALLE_MODEL", "dall-e-3")

# Singleton instance
settings = Settings()