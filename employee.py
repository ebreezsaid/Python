class Employee():
    def __init__(self,emp_id,emp_name,emp_salary,emp_department):
        self.emp_id= emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department  
    def get_emp_id(self):
        return self.emp_id
    def get_emp_name(self):
        return self.emp_name
    def get_emp_salary(self):
        return self.emp_salary
    def get_emp_department(self):
        return self.emp_department
    def set_emp_id(self,newId):
        self.emp_id = newId
    def set_emp_name(self,newName):
        self.emp_name = newName
    def set_emp_salary(self,newSalary):
        self.emp_salary = newSalary
    def set_emp_department(self,newdepartment):
        self.emp_department = newdepartment
        
    def print_employee_details(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)
        print("Employee Department:", self.emp_department)
        
        
    def calculate_emp_salary(self,salary,hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = (overtime * salary) / 50
            return salary + overtime_amount
