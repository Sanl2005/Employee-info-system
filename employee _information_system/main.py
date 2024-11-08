# main.py
from initialize_db import initialize_db
from factories.employee_factory import EmployeeFactory
from dao.employee_dao import EmployeeDAO
from utils.serialization import serialize_employee, deserialize_employee

# Initialize the database
initialize_db()

# Create employees using the factory
factory = EmployeeFactory()
full_time_emp = factory.create_employee("FullTime", "Alice", 75000)
part_time_emp = factory.create_employee("PartTime", "Bob", 30000, hours_per_week=20)
contract_emp = factory.create_employee("Contract", "Charlie", 50000)

# DAO instance
dao = EmployeeDAO()

# Add employees to the database
dao.add_employee(full_time_emp)
dao.add_employee(part_time_emp)
dao.add_employee(contract_emp)

# Retrieve and print employee details
retrieved_employee = dao.get_employee(1)
if retrieved_employee:
    print(f"Retrieved Employee: {retrieved_employee.name}, {retrieved_employee.get_employee_type()}, {retrieved_employee.salary}")

# Serialize and deserialize an employee
serialize_employee(full_time_emp)
deserialized_employee = deserialize_employee()
print(f"Deserialized Employee: {deserialized_employee.name}, {deserialized_employee.get_employee_type()}, {deserialized_employee.salary}")
