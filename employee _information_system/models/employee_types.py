# models/employee_types.py
from .employee import Employee

class FullTimeEmployee(Employee):
    def get_employee_type(self):
        return "Full-Time Employee"

class PartTimeEmployee(Employee):
    def __init__(self, name, salary, hours_per_week):
        super().__init__(name, salary)
        self._hours_per_week = hours_per_week

    @property
    def hours_per_week(self):
        return self._hours_per_week

    def get_employee_type(self):
        return "Part-Time Employee"

class ContractEmployee(Employee):
    def get_employee_type(self):
        return "Contract Employee"
