from common.constants import PRIORITY_VALUE_ERROR
from common.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates


class TodoModel(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    priority = Column(Integer, unique=True)

    @validates("priority")
    def validate_priority(self, _, value):
        if value < 1:
            raise ValueError(PRIORITY_VALUE_ERROR)
        return value
