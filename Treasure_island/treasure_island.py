print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
step1=input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\t').lower()
if step1=="left":
    step2=input("You\'ve come to a lake.There is an island in the middle of the lake.\nType 'wait' to wait for a boat. Type 'swim' to swim across.\t").lower()
    if step2=="wait":
        step3=input("You arrive at the island unharmed.\nThere is house with 3 doors. Red,Yellow and Blue.\nWhich colour do you choose\t").lower()
        if step3=='red':
            print("It's a room full of fire. Game Over")
        elif step3=="blue":
            print("You enter a room of beasts. Game Over.")
        elif step3=="yellow":
            print("You found the treasure.\n!!!YOU WIN!!!\nCongratulations!!!")
        else:
            print("You chose a door that doesn't exist\n Game Over!!!")
    elif step2=="swim":
        print("You got attacked by an angry trout! \nGame Over")
    else:
        print("Game Over!!!")
elif step1=="right":
    print("You fell into a hole.\nGame Over")
else:
    print('You Chose the wrong side.\nGame over!!!')
