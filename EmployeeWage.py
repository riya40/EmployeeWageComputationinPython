import random
"""
Performing the Employee wage computation
checking Employee present or not
Adding the wage_per_day and full_day_hour
"""
print("Welcome to Employee Wage Computation")

WAGE_PER_HR = 20
FULL_DAY_HR = 8


attendence = random.randint(0, 2)

print(f'Attendance {attendence}')

wage_per_day = WAGE_PER_HR * FULL_DAY_HR
print('Wage per day {}'.format(wage_per_day))
