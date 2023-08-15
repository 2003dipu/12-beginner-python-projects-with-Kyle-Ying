"""import random
from words import words as w
import string

def get_valid_word(w):
    word = random.choice(w)
    while '-' in word or ' ' in word:
        word = random.choice(w)
    return word

def hangman():
    word = get_valid_word(w)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives =6


    while len(word_letters) > 0 and lives >0:

        print('You have ',lives, 'lives left and you have used these letters : ', ' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()

        if user_letter not in alphabet:
            print('Invalid character! Please try again.')
            
        
        elif user_letter in used_letters:
            print('You have already used that character. Please try again!')
                
        else:
            lives -=1
            print('Letter is not in word')
        
        used_letters.add(user_letter)

        if user_letter in word_letters:
            word_letters.remove(user_letter)
        else:
            print('Letter not in word.')

        if len(word_letters) == 0:
            print('Congratulations! You guessed the word:', word)
    if lives ==0:
        print('You died. The word was',word)
    else:
        print('You guessed the word',word, '!!')

hangman()
"""
import random
from words import words as w
import string

def get_valid_word(w):
    word = random.choice(w)
    while '-' in word or ' ' in word:
        word = random.choice(w)
    return word

def hangman():
    word = get_valid_word(w)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters:', ' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()

        if user_letter not in alphabet:
            print('Invalid character! Please try again.')
            
        elif user_letter in used_letters:
            print('You have already used that character. Please try again!')
            
        else:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f"Your letter '{user_letter}' is not found in the word. You have {lives} lives left.")

        if len(word_letters) == 0:
            print('Congratulations! You guessed the word:', word)
            
    if lives == 0:
        print('You died. The word was', word)
    else:
        print('You guessed the word', word, '!!')

hangman()
