import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(shift):
    message=""
    for letter in text:
        if letter in range(len(alphabet)-1):
            encode=alphabet.index(letter)+shift
            message+=alphabet[encode]
        else:
            encode=(alphabet.index(letter)+shift)%26
            message += alphabet[encode]
    print(f"Encoded Message:{message}")

def decrypt(shift):
    message=""
    for letter in text:
        if letter in range(len(alphabet)-1):
            decode=alphabet.index(letter)-shift
            message+=alphabet[decode]
        else:
            decode=(alphabet.index(letter)-shift)%26
            message += alphabet[decode]
    print(f"Decoded Message:{message}")

if direction=="encode":
    encrypt(shift)
elif  direction=="decode":
    decrypt(shift)
else:
    print("Please give the correct input.")
