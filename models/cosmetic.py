from typing import Optional
from pydantic import BaseModel

class Cosmetic(BaseModel):
    name: str
    expiryDate: str
    initialQuantity: int
    currentQuantity: Optional[int] = None
    price: float
    family: str
    properties: str[]
    preferedUsage: str