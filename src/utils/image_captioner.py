from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from src.config import settings

# Load model and processor once using configured model name
processor = BlipProcessor.from_pretrained(settings.BLIP_MODEL)
model = BlipForConditionalGeneration.from_pretrained(settings.BLIP_MODEL)

def get_image_caption(image_path: str) -> str:
    """
    Generates a short caption describing the content of an image.

    Args:
        image_path (str): Path to the image file.

    Returns:
        str: Caption describing the image.
    """
    image = Image.open(image_path).convert('RGB')
    inputs = processor(image, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=30)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption
