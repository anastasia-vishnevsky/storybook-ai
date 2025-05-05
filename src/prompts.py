def build_story_prompt(caption: str) -> str:
    """
    Returns a prompt for GPT to generate a children's story based on an image caption.
    """
    return (
        f"Here is a description of an image: '{caption}'. "
        "Write a very short (max 100 words) and very funny children's story based on this image. "
        "The story should be playful, a bit silly, and include magical or unexpected elements."
    )


def build_dalle_prompt(caption: str) -> str:
    """
    Returns a prompt for DALL·E to generate a storybook cover based on the image caption.
    """
    return (
        f"Create an illustration in the style of a children's storybook cover, featuring: {caption}"
    )


def build_gpt_system_prompt() -> str:
    """
    Returns the system prompt to set GPT's behavior.
    """
    return "You are a brilliant and funny children's book author."