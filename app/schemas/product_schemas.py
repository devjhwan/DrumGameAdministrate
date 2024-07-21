from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: float

class ProductCreate(ProductBase):
    description: str

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True
