from sqlalchemy import Column, Table, ForeignKey, Integer
from Models.AppBase import Base

association_table = Table(
    'association',
    Base.metadata,
    Column("user_id", Integer, ForeignKey('users.id')),
    Column("lecture_id", Integer, ForeignKey('lecture.id'))
)
