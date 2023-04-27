from sqlalchemy import Column, Integer

from app.core.db import Base


class Product(Base):
    nm_id = Column(Integer, primary_key=True)
