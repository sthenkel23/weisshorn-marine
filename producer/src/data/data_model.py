from typing import List
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float = 10.5
    tags: List[str] = []


class Price(BaseModel):
    timestamp: str
    amount: float
    base: str
    currency: str

