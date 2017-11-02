import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.User import Base, User

engine = create_engine('sqlite:///Database/database.sqlite3')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# newUser = User(username="Austin",password="admin")
# session.add(newUser)
# session.commit()
#
# newUser = User(username="Bob",password="admin2")
# session.add(newUser)
# session.commit()

users = session.query(User).with_entities(User.username, User.password).all()
print(users)

user = session.query(User).filter(User.username == "Austin", User.password == "admin").first()
print(user)
