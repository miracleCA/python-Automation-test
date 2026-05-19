from pydantic import BaseModel

class Asset(BaseModel):
    id: str
    integrationId: str