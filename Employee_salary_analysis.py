import numpy as np

employee_salaries=np.random.randint(20000,150001,size=500)

print("Employee Highest salary:",np.max(employee_salaries))

print("Employee Lowest salary:",np.min(employee_salaries))

print("Employee Average salary:",np.mean(employee_salaries))

print("Employee Earning more than 100000:",np.sum(employee_salaries>100000))

print("Employee Earning Less than 30000:",np.sum(employee_salaries<30000))

print("Total Salary Expenditure:",np.sum(employee_salaries))