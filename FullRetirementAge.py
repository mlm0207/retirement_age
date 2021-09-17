from AgeCalculator import RetirementAgeCalculator
from datetime import date

print("Social Security Full Retirement Age Calculator")


try:

    year_of_birth = int(input("Enter the year of birth or to exit "))

    while 1900 <= year_of_birth <= date.today().year:

        month_of_birth = int(input("Enter the month of birth "))
        retirement = RetirementAgeCalculator(year_of_birth, month_of_birth)
        print("your full retirement age is", retirement.retirement_age, "and", retirement.retirement_months, "months")
        print("this will be in", retirement.month_of_retirement, "of", retirement.year_of_retirement)
        print("")
        year_of_birth = int(input("Enter the year of birth or to exit "))

except ValueError:
    exit(0)

