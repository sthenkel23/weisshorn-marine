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
    amount: float = None
    base: str = None
    currency: str = None
    pred: float = None
    pred_up: float = None
    pred_dw: float = None
