import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options=[rock,paper,scissors]
computer_choice=random.randint(0,2)
my_choice=int(input("What do you chose?. 0 for Rock, 1 for paper and 2 for scissors"))

print(f"Your Choice:{my_choice}\n{(options[my_choice])}")
print(f"Computer Choice:{computer_choice}\n{options[computer_choice]}")

if my_choice == computer_choice:
    print("Its Draw")
elif my_choice==0 and computer_choice ==2:
    print("You Win")
elif my_choice == 1 and computer_choice == 0:
    print("You Win")
elif my_choice==2 and computer_choice==1:
    print("You Win")
elif my_choice==0 and computer_choice==1:
    print("You Lost")
elif my_choice == 1 and computer_choice == 2:
    print("You Lost")
elif my_choice==2 and computer_choice==0:
    print("You Lost")
else:
    print("Wrong Input")
