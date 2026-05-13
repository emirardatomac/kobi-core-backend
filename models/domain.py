from sqlalchemy import Column, Integer, String
from database.config import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer = Column(String, index=True)
    status = Column(String)


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    product = Column(String, index=True)
    stock = Column(Integer)


class Cargo(Base):
    __tablename__ = "cargo"

    id = Column(Integer, primary_key=True, index=True)
    tracking = Column(String, unique=True, index=True)
    status = Column(String)