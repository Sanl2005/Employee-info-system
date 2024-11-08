# factories/employee_factory.py
from models.employee_types import FullTimeEmployee, PartTimeEmployee, ContractEmployee

class EmployeeFactory:
    @staticmethod
    def create_employee(emp_type, name, salary, hours_per_week=None):
        if emp_type == "FullTime":
            return FullTimeEmployee(name, salary)
        elif emp_type == "PartTime":
            return PartTimeEmployee(name, salary, hours_per_week)
        elif emp_type == "Contract":
            return ContractEmployee(name, salary)
        else:
            raise ValueError(f"Unknown employee type: {emp_type}")
