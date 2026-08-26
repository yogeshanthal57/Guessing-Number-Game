# import random 
# print("\n🎯Welcome to the Guessing Number Game🎮 ")
# print("I have selected a number between 1 to 100.")
# print("You have 3 attempt to guess it.")
# secret_number=random.randint(1,100)
# attempt=0
# max_attempt=3
# for attempt in range(1,max_attempt+1):
#     guess=int(input(f"{attempt}.Guessing the Number : "))
#     attempt+1
#     if secret_number==guess:
#         print("Congratulation! you win")
#         print(f"secret number was{secret_number}")
#         break

#     elif guess<secret_number:
#         print("Too high")
#     else:
#         print("Too low")
#     if (attempt<max_attempt):
#         print("Try again 🔄 ")
#     else:
#         print("Game over!\nBetter luck next time ")
#         print(f"secret number was {secret_number}")

import random

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))

print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")

num = random.randint(low, high) 
# Total allowed chances
ch = 7 
# Guess counter
gc = 0                         

while gc < ch:
    gc += 1
    guess = int(input('Enter your guess: '))

    if guess == num:
        print(f'Correct! The number is {num}. You guessed it in {gc} attempts.')
        break

    elif gc >= ch and guess != num:
        print(f'Sorry! The number was {num}. Better luck next time.')

    elif guess > num:
        print('Too high! Try a lower number.')

    elif guess < num:
        print('Too low! Try a higher number.')

    
