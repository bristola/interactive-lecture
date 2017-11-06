import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.Models import Base, User, Lecture

engine = create_engine('sqlite:///interlect/Database/database.sqlite3')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# lecture = Lecture(name="CMPSC1000",owner=2,school="Allegheny")
# session.add(lecture)
# session.commit()

# lecture = session.query(Lecture).filter(Lecture.name == "CMPSC1000").first()
# users = session.query(User).filter(User.username != "Teacher").all()
# print(type(users))
# lecture.users = users
# session.commit()

lecture = session.query(Lecture).filter(Lecture.name == "lecture1").first()
print(lecture.users)
print(lecture.owner)
print(lecture.ownerObj)

# lecture = session.query(Lecture).filter(Lecture.name == "lecture1").first()
# user = session.query(User).filter(User.username == "Austin").first()
# print(lecture)
# lecture.ownerObj = user
# session.commit()
