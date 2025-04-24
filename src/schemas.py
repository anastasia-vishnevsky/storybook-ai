from pydantic import BaseModel

class StorybookResponse(BaseModel):
    caption: str
    story: str
    cover_url: str