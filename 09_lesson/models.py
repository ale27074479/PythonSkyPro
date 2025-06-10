from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from database import DATABASE_URL

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)  # Для soft delete
    