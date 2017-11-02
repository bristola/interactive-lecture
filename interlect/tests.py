import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.User import Base, User
from Models.Lecture import Lecture

engine = create_engine('sqlite:///interlect/Database/database.sqlite3')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

user = session.query(User).filter(User.username =="Teacher").first()
print(user.lectures)
