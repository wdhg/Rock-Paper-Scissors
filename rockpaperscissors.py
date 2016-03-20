import random
import math

VALID_CHOICES = ["rock", "paper", "scissors"]
# These are all the possible matches where the player wins
PLAYER_WINS = ["rock vs scissors", "scissors vs paper", "paper vs rock"]
# This will store the name of the person who won each game
wins = []
# The amount of games the player has to win to win the whole game
MINIMUM_GAMES = 2
PLAYER = "Player"
AI = "Ai"

def get_choice():
    # Gets input from user and makes sure it is valid
    choice = input("Enter rock, paper, or scissors\n").lower()
    while choice not in VALID_CHOICES:
        choice = input("Enter valid choice: rock, paper, or scissors\n").lower()
    else:
        return choice

def ai_choice():
    return random.choice(VALID_CHOICES)

# Compares choices to find who wins the round
def compare_choices(player_choice, ai_choice):
    message = player_choice + " vs " + ai_choice
    print("\n" + message)
    if ai_choice == player_choice:
        print("Draw\n")
    else:
        # If the message is in the list PLAYER_WINS, the player wins
        # Else the ai wins
        if message in PLAYER_WINS:
            print("Player wins\n")
            wins.append(PLAYER)
        else:
            print("Ai wins\n")
            wins.append(AI)

def game_over():
    # If the player / ai has won the amount of required game
    if wins.count(PLAYER) == MINIMUM_GAMES:
        print("Player wins the game!")
        return True
    elif wins.count("Ai") == MINIMUM_GAMES:
        print("Ai wins the game!")
        return True
    return False

def play():
    while not game_over():
        compare_choices(get_choice(), ai_choice())

play()
