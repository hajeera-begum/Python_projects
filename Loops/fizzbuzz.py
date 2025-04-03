# This program prints numbers from 1 to 100.
# - For numbers divisible by 3, it prints "Fizz".
# - For numbers divisible by 5, it prints "Buzz".
# - For numbers divisible by both 3 and 5, it prints "FizzBuzz".
# - Otherwise, it prints the number itself.
for i in range(1,101):
    if i%3==0 and i%5==0:
        i="FizzBuzz"
        print(i)
    elif i % 5==0:
        i="Buzz"
        print(i)
    elif i%3==0:
        i="Fizz"
        print(i)
    else:
        print(i)
