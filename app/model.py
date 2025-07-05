from pydantic import BaseModel

class CarInput(BaseModel):
    year: int
    mileage: float
    fuel_type: int
    transmission: int
    owner: int
