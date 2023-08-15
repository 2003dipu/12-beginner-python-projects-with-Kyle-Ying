"""import random # (using function and if else statement)

def is_win(user,computer):
        # returns true if player wins
        if (user == 'r' and computer == 's') or user == 's' and computer == 'p'\
            or (computer == 'p' and computer == 'r'):
            return True
    

def play():
    user = input("What's your choice? 'r' for rock,'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s tie'
    if is_win(user,computer):

        return 'You won'
    return 'You Lost'

    # r>s (rock beats scissors), paper > scissors(paper beats scissors), scissors > paper(scissors beats paper)
print(play())"""
# Alternative code (using while loop and if else statement)
import random

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock")\
        or (player == "scissors" and computer == "paper"):
        print("You win!")
        print("You have defeated the computer !")
    else:
        print("You lose!")
        print("Computer Win")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")