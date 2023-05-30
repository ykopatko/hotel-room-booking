from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic.schema import Decimal


class CategoryBase(BaseModel):
    name: str
    description: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str
    description: str
    price: int
    quantity: int
    created_at: Optional[datetime] = None


class ProductCreate(ProductBase):
    category_id: int


class Product(ProductBase):
    id: int
    category: Category

    class Config:
        orm_mode = True
