from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from Models.Association import association_table
from Models.AppBase import Base


class Lecture(Base):
    __tablename__ = 'lecture'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    users = relationship(
        "User",
        secondary=association_table,
        back_populates="lectures")

    def __repr__(self):
        return "%d/%s" % (self.id, self.name)
