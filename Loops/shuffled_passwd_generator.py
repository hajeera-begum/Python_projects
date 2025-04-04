# A simple Python script that generates a random password based on user input.
# The user specifies the number of letters, numbers, and symbols they want in the password.
# The script then randomly selects characters from each category, shuffles them, and outputs the final password.

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Pypassword_list Generator!")
nr_letters = int(input("How many letters would you like in your password_list?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list=[]

for i in range(0,nr_letters):
    random_letter=random.choice(letters)
    password_list+=random_letter

for j in range(0,nr_numbers):
    random_number=random.choice(numbers)
    password_list+=random_number

for k in range(0,nr_symbols):
    random_symbol=random.choice(symbols)
    password_list+=random_symbol

random.shuffle(password_list)
password=''.join(password_list)
print(password)
