# utils/serialization.py
import pickle

def serialize_employee(employee, filename='employee_data.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(employee, file)

def deserialize_employee(filename='employee_data.pkl'):
    with open(filename, 'rb') as file:
        return pickle.load(file)
