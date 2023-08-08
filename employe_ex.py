import pandas as pd

class Employee:
    def __init__(self, name, idd, salary):
        self.name = name
        self.idd = idd
        self.salary = salary

def read_employees_from_excel(file_name):
    employees = []
    try:
        df = pd.read_excel(file_name)
        for index, row in df.iterrows():
            name, idd, salary = row["name"], row["idd"], row["salary"]
            employee = Employee(name=name, idd=idd, salary=salary)
            employees.append(employee)
    except Exception as e:
        print(f"Error while reading employees from Excel: {e}")
    return employees

def binary_search_employees(employees, target_id):
    left, right = 0, len(employees) - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_emp_id = employees[mid].idd
        if mid_emp_id == target_id:
            return employees[mid]
        elif mid_emp_id < target_id:
            left = mid + 1
        else:
            right = mid - 1
    return None

if __name__ == "__main__":
    excel_file = "e.xlsx"

    
    employees = read_employees_from_excel(excel_file)
    employees.sort(key=lambda x: x.idd)

    
    target_id = 7  
    result = binary_search_employees(employees, target_id)
    if result:
        print(f"Employee found: Name: {result.name}, ID: {result.idd}, Salary: {result.salary}")
    else:
        print("Employee not found.")
