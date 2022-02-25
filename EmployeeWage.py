import random

"""
Performing the Employee wage computation
checking Employee present or not
Adding the wage_per_day and full_day_hour
Adding the parttimer and hour
"""
print("Welcome to Employee Wage Computation")

WAGE_PER_DAY = 20
FULL_DAY_HOUR = 8
PART_TIMER = 6  # adding parttime wage

attendance = random.randint(0, 2)


# adding switchcase:
wage_calculation = {
        0: {'attendance': 'absent', 'wage': 0, 'worked_hr': 0},
        1: {'attendance': 'present', 'wage': WAGE_PER_DAY, 'worked_hr': FULL_DAY_HOUR},
        2: {'attendance': 'part-time', 'wage': WAGE_PER_DAY, 'worked_hr': PART_TIMER}
    }
print('Wage according to attendance :', wage_calculation.get(attendance))
