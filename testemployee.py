from employee import Employee
def main():
    
    emp1 = Employee("ADAMS","E7876",50000,"ACCOUNTING")
    print(emp1.get_emp_id())
    print(emp1.get_emp_name())
    print(emp1.get_emp_salary())
    print(emp1.get_emp_department())
    ####
    emp2 = Employee("JONES", "E7499", 45000, "RESEARCH")
    print(emp2.get_emp_id())
    print(emp2.get_emp_name())
    print(emp2.get_emp_salary())
    print(emp2.get_emp_department())
    ####
    emp3 = Employee("MARTIN", "E7900", 50000, "SALES")
    print(emp3.get_emp_id())
    print(emp3.get_emp_name())
    print(emp3.get_emp_salary())
    print(emp3.get_emp_department())
    ####
    emp4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")
    print(emp4.get_emp_id())
    print(emp4.get_emp_name())
    print(emp4.get_emp_salary())
    print(emp4.get_emp_department())
    #####
    
    #1
    emp1.set_emp_department("TEACHER")
    print(emp1.get_emp_department())
    
    #2
    emp1.print_employee_details()
     
     
    #3 
    salary = 15000
    hours_worked = 60
    calculate_salary = (emp1.calculate_emp_salary(salary,hours_worked))
    print("calculate salary:", calculate_salary)
main()