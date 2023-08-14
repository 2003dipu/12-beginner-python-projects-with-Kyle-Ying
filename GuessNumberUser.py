# In this number guessing game the user is going to generate a number and the computer has to guess it correctly
import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x} : '))
        if guess < random_number:
            print("Incorrect, guess again. Too low! ")
        elif guess > random_number:
            print("Incorrect, guess again. Too high!")
    print(f"Yay, congrats. You have guessed the number {random_number} correctly.\
YOU WIN!")
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c'.lower():
        guess = random.randint(low,high)
        # Human(user) will give feedback to the computer based on the number computer guesses.
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low # could also be high because low =high
        # every variable inside of input function is shown along with the prompt. So you don't need to print it
        feedback = input(f"Is {guess} too high (H), too low(L), or correct (C) ?? : ").lower() 
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l': # if the computer generated number is lower than the guess which the user sets
            low = guess +1 # then computer will need to guess more higher number to get the reward
    print(f"Yay, computer has guessed your number, {guess} , correctly!")

computer_guess(100)