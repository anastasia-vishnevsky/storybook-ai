from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load model and processor once on module import
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

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
    output = model.generate(**inputs)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption
