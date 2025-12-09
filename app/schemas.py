from pydantic import BaseModel, Field


class ProductSchema(BaseModel):
    product_id: int
    name: str = Field(max_length=64)
    category: str = Field(max_length=64)
    price: float = Field(ge=0)
    in_stock: bool
