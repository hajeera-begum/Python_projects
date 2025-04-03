import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
paybill= random.randint(0,len(friends)-1)
a=friends[paybill]
print(f"{a} should pay the bill")
