print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill=5
        print("Please pay $5.")
    elif age <= 18:
        bill=7
        print("Please pay $7.")
    else:
        bill=12
        print("Please pay $12.")
    want_photo=input("Do you need photos? Y or N ?")
    if want_photo=='Y':
        bill+=3

    print(f"Your total ticket is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
