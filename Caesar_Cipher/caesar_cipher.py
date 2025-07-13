import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift_amount, encode_or_decode):
    message=""
    if encode_or_decode=="decode":
        shift_amount*=-1
    for letter in text:
        if letter in alphabet:
            index=(alphabet.index(letter))
            new_index = (index+shift_amount)%26
            message+=alphabet[new_index]
        else:
            message += letter
    print(f"{encode_or_decode}d Message:{message}")

should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    repeat=input("Would you like to continue? Type 'Yes' or 'No'").lower()
    if repeat=="no":
        print("Thank You for your visit\nGood Bye")
        should_continue=False
