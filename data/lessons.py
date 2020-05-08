import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Lesson(SqlAlchemyBase):
    __tablename__ = 'lessons'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    subject_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("subjects.id"))
    teacher_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("teachers.id"))
    date = sqlalchemy.Column(sqlalchemy.DateTime)

    subject = orm.relation('Subject')
    teacher = orm.relation('Teacher')
    attendances = orm.relation("Attendance", back_populates='lesson')
    groups = orm.relation("Group",
                              secondary="group_to_lesson",
                              backref="groups")