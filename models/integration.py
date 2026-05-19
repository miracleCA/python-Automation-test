from pydantic import BaseModel

class Integration(BaseModel):
    id: str
    name: str