import logging
from pathlib import Path

# Set up logs/ directory
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Create a logger
logger = logging.getLogger("storybook")
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler(LOG_DIR / "app.log")
file_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
file_handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(file_handler)
