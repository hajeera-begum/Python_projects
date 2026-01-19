## Real-World Problem: Simple Bank Account Simulation

**Problem Statement:**

You need to create a simple command-line bank account simulation. Users should be able to perform basic banking operations like checking their balance, making deposits, and making withdrawals. The program should handle invalid inputs and insufficient funds.

**Task:**

Write a Python program that simulates a bank account with the following features:

1.  **Initial Balance:** Start with a predefined initial balance.
2.  **Menu:** Present the user with a menu of options: Check Balance, Deposit, Withdraw, and Exit.
3.  **User Input:** Get the user's choice from the menu.
4.  **Conditional Logic:** Use `if-elif-else` statements to perform actions based on the user's choice.
5.  **Deposit:** If the user chooses deposit, ask for the deposit amount. Ensure the amount is positive before adding it to the balance.
6.  **Withdrawal:** If the user chooses withdrawal, ask for the withdrawal amount. Check if the amount is positive and if there are sufficient funds before subtracting it from the balance.
7.  **Check Balance:** If the user chooses to check balance, display the current balance.
8.  **Looping:** Use a `while` loop to keep the program running until the user chooses to exit.
9.  **Input Validation:** Handle cases where the user enters non-numeric input for amounts (you can use `try-except` blocks for more robust handling, but for this basic exercise, you can use string methods like `isdigit()` and conditional statements).
10. **Exit:** If the user chooses exit, end the program using `break`.

**Steps to Solve:**

1.  Initialize a variable for the `balance`.
2.  Create a `while True` loop for the main program loop.
3.  Inside the loop, display the menu of options.
4.  Get the user's `choice` using `input()`.
5.  Use `if-elif-else` to handle each `choice`:
    *   For "Check Balance", print the current `balance`.
    *   For "Deposit", get the `deposit_amount`, validate it, and update the `balance`.
    *   For "Withdraw", get the `withdrawal_amount`, validate it, check for sufficient funds, and update the `balance`.
    *   For "Exit", print a goodbye message and `break` out of the loop.
    *   For any other input, print an "Invalid choice" message.
6.  Consider adding basic input validation for deposit and withdrawal amounts (e.g., checking if the input is a positive number).
