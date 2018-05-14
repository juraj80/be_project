from sqlalchemy.orm import joinedload

from ems_app.data.employee import Employee
from ems_app.data.dbsession import DbSessionFactory
#from ems_app.data.track import Track


class EmpsService:
    @staticmethod
    def get_emps():
        session = DbSessionFactory.create_session()

        emps = session.query(Employee).order_by(Employee.birth_date.desc()).all()
        return emps

    @classmethod
    def create_employee(cls, first_name: str, last_name: str, birth_date: int, gender: str ,salary: float, emp_image: str, dept_name:str):
        session = DbSessionFactory.create_session()

        employee = Employee(first_name=first_name, last_name=last_name,birth_date=birth_date, gender=gender, salary=salary, emp_image=emp_image, dept_name=dept_name)

        session.add(employee)

        session.commit()
        return employee
