# models/employee_types.py

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_employee_type(self):
        raise NotImplementedError("Subclass must implement this method")


class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.type = "Full-Time"  # Add type attribute

    def get_employee_type(self):
        return "Full-Time Employee"


class PartTimeEmployee(Employee):
    def __init__ (self, name, salary, hours_per_week):
        super().__init__(name, salary)
        self.type = "Part-Time"  # Add type attribute
        self.hours_per_week = hours_per_week

    def get_employee_type(self):
        return "Part-Time Employee"


class ContractEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.type = "Contract"  # Add type attribute

    def get_employee_type(self):
        return "Contract Employee"


