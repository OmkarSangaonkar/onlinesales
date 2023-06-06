"""
task 1 sql quries

SELECT d.department_name, AVG(e.salary) AS average_salary
FROM departments d
JOIN employees e ON d.id = e.department_id
GROUP BY d.department_name
ORDER BY average_salary DESC;


"""


"""
task 2 script

import csv

def generate_report():
    with open('employees.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Process and generate report based on row data
            # Example: print(row)

generate_report()

"""



"""
task 3 python code

def compute_result(n):
    if n < 10:
        return n ** 2
    elif n >= 10 and n <= 20:
        fact = 1
        for i in range(1, n - 9):
            fact *= i
        return fact
    elif n > 20:
        return sum(range(1, n - 19))

# Test cases
print(compute_result(4))   # Output: 16
print(compute_result(15))  # Output: 120
print(compute_result(25))  # Output: 15

"""