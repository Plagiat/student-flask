import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Group(SqlAlchemyBase):
    __tablename__ = 'groups'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    entrance_year = sqlalchemy.Column(sqlalchemy.Integer)

    students = orm.relation("Student", back_populates='group')
    lessons = orm.relation("Lesson",
                          secondary="group_to_lesson",
                          backref="lessons")


group_to_lesson_table = sqlalchemy.Table('group_to_lesson', SqlAlchemyBase.metadata,
    sqlalchemy.Column('lessons', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('lessons.id')),
    sqlalchemy.Column('groups', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('groups.id'))
)