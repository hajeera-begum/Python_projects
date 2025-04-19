## Main game logic 
import random
from  hangman_words import word_list
from hangman_art import stages,logo

lives = 6

print(logo)
chosen_word = random.choice(word_list)
#print(chosen_word)

word_to_guess=''
for characters in range(len(chosen_word)):
    word_to_guess+="_"
print(f"Word to Guess: {word_to_guess}")

game_over = False
correct_letters = []

while not game_over:

    print(f"\n**************************** {lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    display =""
    if guess in correct_letters:
        print(f"You have already guessed {guess}.")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
             display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        print(f"You guessed {guess},that's not in the word.You lose a life")
        lives -= 1

        if lives == 0:
            game_over = True
            print(f"IT WAS {chosen_word} ")
            print(f"***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])

