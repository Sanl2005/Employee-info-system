# models/employee.py
from .person import Person

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    def get_employee_type(self):
        return "General Employee"
