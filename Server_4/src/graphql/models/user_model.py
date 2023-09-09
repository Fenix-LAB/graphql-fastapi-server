from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class User(Base):
    __tablename__ = "users"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(100))
    # name: str = Column(String, nullable=False, unique=True)

    stickynotes = relationship("StickyNotes", cascade="all, delete", passive_deletes=True)

    def __init__(self, name: str):
        self.name = name

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }