from pydantic import BaseModel


class JobCreate(BaseModel):
    image_url: str
    callback_url: str
    callback_token: str
    algorithm_name: str


