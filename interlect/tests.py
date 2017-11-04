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

lectures = session.query(Lecture).filter(Lecture.owner == 1).all()
print(lectures)
