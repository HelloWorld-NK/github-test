from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BookModel(Base):
    __tablename__ = "books"

    title = Column(String, primary_key=True)
    author = Column(String)
    category = Column(String)
