from typing import List, Annotated

from fastapi import FastAPI, Query
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field

from .database import get_db, engine, Base
from .models import Product
from .schemas import ProductSchema

app = FastAPI()

Base.metadata.create_all(engine)


# @app.get('/products', response_model=List[ProductSchema])
# def get_products():
#     db: Session = get_db()

#     result = db.query(Product).all()

#     return result


# @app.get('/products/{product_id}', response_model=ProductSchema)
# def get_product_by_id(product_id: int):
#     db: Session = get_db()

#     result = db.query(Product).get(product_id)

#     return result


class QueryParams(BaseModel):
    min_price: float| None = Field(None, ge=0)
    max_price: float | None = Field(None, ge=0)
    limit: int = Field(ge=0)
    offset: int = Field(ge=0)


@app.get('/product-list/')
def get_product_list(
    query_params: QueryParams = Query()
) -> List[ProductSchema]:
    db: Session = get_db()

    result = db.query(Product).filter(
        Product.price.between(query_params.min_price, query_params.max_price)
    ).offset(query_params.offset).limit(query_params.limit).all()

    return result

