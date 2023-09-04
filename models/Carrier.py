from pydantic import BaseModel

class Carrier(BaseModel):
    carrier_code: str
    id: int
    name: str
