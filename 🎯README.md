# 🎯 Number Guessing Game

A simple **Number Guessing Game built with Python**. The computer randomly selects a number between the lower and upper bounds entered by the user. The player gets **7 chances** to guess the correct number.

## 📌 Features

- 🎲 Generates a random number using Python's `random` module.
- 🔢 User can choose the lower and upper bounds.
- 🎯 Player gets 7 chances to guess the number.
- ⬆️ Shows **"Too high"** when the guess is greater than the secret number.
- ⬇️ Shows **"Too low"** when the guess is smaller than the secret number.
- 🏆 Displays a winning message when the correct number is guessed.
- ❌ Shows the correct number when all attempts are used.

## 🛠️ Technologies Used

- **Python 3**
- **Random Module**

## 🚀 How to Run

1. Make sure Python is installed on your computer.
2. Download or clone this repository.
3. Open the project folder in Terminal or Command Prompt.
4. Run the following command:

```bash
python Gussing_number_game.py
```

5. Enter the **Lower Bound**.
6. Enter the **Upper Bound**.
7. Start guessing the number.

## 🎮 How the Game Works

The program first asks the user to enter the lower and upper limits. It then randomly generates a number within that range.

The player has **7 attempts** to guess the number. After each guess, the program provides a hint:

- **Too high!** → Guess a smaller number.
- **Too low!** → Guess a larger number.
- **Correct!** → You win the game.

## 📷 Example

```text
Hi! Welcome to the Number Guessing Game.
You have 7 chances to guess the number. Let's start!

Enter the Lower Bound: 1
Enter the Upper Bound: 100

You have 7 chances to guess the number between 1 and 100. Let's start!

Enter your guess: 50
Too high! Try a lower number.

Enter your guess: 25
Too low! Try a higher number.

Enter your guess: 37
Correct! The number is 37. You guessed it in 3 attempts.
```

## 📂 Project Structure

```text
Number-Guessing-Game/
│
├── Gussing_number_game.py
└── README.md
```

## 👨‍💻 Author

**Yogesh**

BCA Final Year Student

## ⭐ Future Improvements

- Add difficulty levels.
- Allow the player to play again without restarting the program.
- Add a score system.
- Add a limited-time challenge.
- Add a graphical user interface (GUI).