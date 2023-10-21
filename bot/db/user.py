import datetime

from sqlalchemy import Column, Integer, VARCHAR

from .base import BaseModel

class User(BaseModel):
    __tablename__ = 'users'

    user_id = Column(Integer, unique=True, nullable=False, primary_key=True)

    username = Column(VARCHAR(32), unique=False, nullable=True)

    victim = Column(Integer, default=None)


    def __str__(self) -> str:
        return f"<User:{self.user_id}"