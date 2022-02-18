import random
"""
Performing the Employee wage computaion
checking Employee present or not
"""
print("Welcome to Employee Wage Computation")

attendence = random.randint(0, 1)

if attendence == 1:
    print("employee is present:", attendence)
else:
    print("employee is absent:", attendence)