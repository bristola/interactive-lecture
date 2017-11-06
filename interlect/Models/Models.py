from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from flask.ext.login import UserMixin


Base = declarative_base()


association_table = Table(
    'association',
    Base.metadata,
    Column("user_id", Integer, ForeignKey('users.id')),
    Column("lecture_id", Integer, ForeignKey('lecture.id'))
)


class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)
    owned_lectures = relationship("Lecture",back_populates="ownerObj")
    lectures = relationship(
        "Lecture",
        secondary=association_table,
        back_populates="users")

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.username, self.password)


class Lecture(Base):
    __tablename__ = 'lecture'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    owner = Column(Integer, ForeignKey(User.id), primary_key=True)
    ownerObj = relationship("User",back_populates="owned_lectures")
    school = Column(String(30), nullable=False)
    users = relationship(
        "User",
        secondary=association_table,
        back_populates="lectures")

    def __repr__(self):
        return "%d/%s" % (self.id, self.name)
