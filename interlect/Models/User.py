from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask.ext.login import UserMixin
from Models.Association import association_table
from Models.AppBase import Base
from Models.Lecture import Lecture


class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)

    lectures = relationship(
        "Lecture",
        secondary=association_table,
        back_populates="users")

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.username, self.password)
