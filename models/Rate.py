from pydantic import BaseModel


class Rate(BaseModel):
    delivery_date: str
    total_cost: float
    valid: bool
    response_time_in_seconds: float
