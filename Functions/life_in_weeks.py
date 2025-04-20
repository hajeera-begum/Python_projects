# Life in Weeks

#A simple Python program that calculates the number of weeks you have left to live, assuming a lifespan of 90 years.

## How to Use

#1. Run the script:  python life_in_weeks.py


def life_in_weeks(age):
    weeks_left=(90-age)*52
    print(f"You have {weeks_left} weeks left.")

current_age=int(input("Please Enter your current age:"))
life_in_weeks(current_age)

#Example Output
#Please Enter your current age: 25
#You have 3380 weeks left.
