from sqlalchemy import Column, Integer, String
from .configurations import Base


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))
