# 💖 Love Calculator

#A fun Python program that calculates a "love score" based on the names of two individuals.

## How It Works

#The program:
#- Combines both names into a single string.
#- Counts the occurrences of the letters in the words "TRUE" and "LOVE".
#- Calculates two separate totals:
#  - The sum of counts for 'T', 'R', 'U', 'E'.
#  - The sum of counts for 'L', 'O', 'V', 'E'.
#- Concatenates these two totals to form a love score.

## Usage

#Run the script and follow the prompts: python love_calculator.py

##Example Output
#Please enter the first name: Alice
#Please enter the second name: Bob
#Your love score is: 56
 
def calculate_love_score(name1,name2):
    namesmerge=name1+name2
    t=namesmerge.count('t')
    r=namesmerge.count('r')
    u=namesmerge.count('u')
    e=namesmerge.count('e')
    digit1=t+r+u+e
    #print(f"{t}{r}{u}{e}")
    l=namesmerge.count('l')
    o=namesmerge.count('o')
    v=namesmerge.count('v')
    e=namesmerge.count('e')
    #print(f"{l}{o}{v}{e}")
    digit2=l+o+v+e
    print(f"{digit1}{digit2}")
    
parameter1=str(input("Please enter the first name: ")).lower()
parameter2=str(input("Please enter the second name: ")).lower()
calculate_love_score(parameter1,parameter2)
