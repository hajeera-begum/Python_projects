# Hangman Game 🎯

This is a simple command-line Hangman game built using Python.

## 📌 Description

In this game, a random word is selected, and the player needs to guess the word by entering one letter at a time. The player has 6 lives, and each incorrect guess reduces one life. The game ends when:
- The player successfully guesses all letters (🎉 WIN)
- The player runs out of lives (💀 LOSE)

The game uses custom ASCII art (`hangman_art.py`) and a word list (`hangman_words.py`) for added fun.

## 🛠️ Features

- Random word selection
- Tracks correct guesses
- Shows hangman stages visually
- Ends game on win or lose condition
- Warns if a correct letter was guessed again

## 📂 Project Structure
Hangman/ ├── hangman.py # Main game logic 
         ├── hangman_words.py # Contains word_list 
         ├── hangman_art.py # Contains logo and stages (ASCII art) └
         ├── README.md # This file

## ▶️ How to Run

1. Clone the repository or download the files.
2. Make sure Python is installed on your system.
3. Run the game using:

```bash
python hangman.py
```

📌 To Do (Future Enhancements)
 - Add logic to warn: "You have already guessed this wrong letter."
 - Show list of all guessed letters

🧑‍💻 Author
Hajeera Begum
Python Developer | Automation Enthusiast
📫 hajbegu1@gmail.com
