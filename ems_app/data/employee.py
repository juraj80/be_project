import sqlalchemy
import sqlalchemy.orm
from sqlalchemy.ext.orderinglist import ordering_list

from ems_app.data.modelbase import SqlAlchemyBase


class Employee(SqlAlchemyBase):
    __tablename__ = 'Employee'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, unique=True, autoincrement=True)
    first_name = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=False)
    last_name = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=False)

    birth_date = sqlalchemy.Column(sqlalchemy.String, index=True)
    gender = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=False)
    salary = sqlalchemy.Column(sqlalchemy.Float, index=True)
    emp_image = sqlalchemy.Column(sqlalchemy.String)
    dept_name = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=False)
    # has_preview = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    # is_published = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

