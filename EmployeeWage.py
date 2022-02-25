import random

"""
Performing the Employee wage computation
checking Employee present or not
Adding the wage_per_day and full_day_hour
Adding the parttimer and hour
"""
print("Welcome to Employee Wage Computation")

WAGE_PER_HR = 20
FULL_DAY_HR = 8
PART_TIME_HR = 6  # adding parttime wage

attendance = random.randint(0, 2)

if attendance == 0:
    print("absent")
elif attendance == 1:  # adding partime
    hours = PART_TIME_HR
    wage = PART_TIME_HR * WAGE_PER_HR
    print("Today Present but par time wage is", wage, hours)
else:
    hours = FULL_DAY_HR
    wage = FULL_DAY_HR * WAGE_PER_HR
    print("today present and for full day", wage, hours)
