# In this number guessing game the computer is going to generate a number and the user has to guess it correctly
import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x} : '))
        # Computer will give feedback to the user based on what user guesses
        if guess < random_number:
            print("Incorrect, guess again. Too low! ")
        elif guess > random_number:
            print("Incorrect, guess again. Too high!")
    print(f"Yay, congrats. You have guessed the number {random_number} correctly.\
YOU WIN!")
guess(10)