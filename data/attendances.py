import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Attendance(SqlAlchemyBase):
    __tablename__ = 'attendances'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    lesson_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("lessons.id"))
    student_id= sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("students.id"))

    presence = sqlalchemy.Column(sqlalchemy.Boolean)

    lesson = orm.relation('Lesson')
    student = orm.relation('Student')