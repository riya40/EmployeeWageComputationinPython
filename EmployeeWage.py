import random

"""
Performing the Employee wage computation
checking Employee present or not
Adding the wage_per_day and full_day_hour
Adding the parttimer and hour
adding solving switch statement
Assume the working day
"""
print("Welcome to Employee Wage Computation")

WAGE_PER_DAY = 20
FULL_DAY_HOUR = 8
PART_TIMER = 6  # adding parttime wage
WORKING_DAY_PER_MONTH = 20
working_day_count = 0
pay = 0
calculating_hours = 0
total_wage = 0
calculating_wage = 0
working_hours = 0


while WORKING_DAY_PER_MONTH > working_day_count:
    attendance = random.randint(0, 2)

    # adding switchcase:
    wage_calculation = {
            0: {'attendance': 'absent', 'wage': 0, 'worked_hr': 0},
            1: {'attendance': 'present', 'wage': WAGE_PER_DAY, 'worked_hr': FULL_DAY_HOUR},
            2: {'attendance': 'part-time', 'wage': WAGE_PER_DAY, 'worked_hr': PART_TIMER}
        }
    status = wage_calculation.get(attendance)
    pay = status.get('wage')
    working_hours += status.get('worked_hr')
    pay_calculating = pay * working_hours
    calculating_wage += pay_calculating
    calculating_hours += status.get('worked_hr')
    working_day_count += 1
total_wage += pay_calculating
print("totalwage:", total_wage)
print("totalhours:", calculating_hours)