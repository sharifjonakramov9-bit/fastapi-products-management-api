from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
)

from .database import Base


class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True)
    name = Column(String(length=64), nullable=False)
    category = Column(String(length=64), nullable=False)
    price = Column(Float, nullable=False)
    in_stock = Column(Boolean, nullable=False, default=True)

    def __str__(self):
        return self.name   

    def __repr__(self):
        return self.name
