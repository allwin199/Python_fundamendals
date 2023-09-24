import sys
import random


def valid_choice(player):
    if player not in ["1", "2", "3"]:
        print("\nYou must enter 1,2 or 3")
        start_game()
    else:
        return


def options_chosen(val):
    if val == 1:
        return "Rock"
    elif val == 2:
        return "Paper"
    elif val == 3:
        return "Scissors"


def user_won():
    print("\n🎉 You Won!")


def python_won():
    print("\n🐍 Python Won!")


def tie():
    print("\n👍 Tie!")


def who_won(player, computer):
    if player == computer:
        tie()
    elif player == 1 and computer == 3:
        user_won()
    elif player == 2 and computer == 1:
        user_won()
    elif player == 3 and computer == 2:
        user_won()
    else:
        python_won()


def game_restart():
    restart = input("\nPlay Again? \n\npress 'Y' If not press 'Q' to quit : ")

    if restart.lower() not in ["y", "q"]:
        print("\nChoose 'Y' to play or 'Q' to quit")
        game_restart()

    while restart.lower() == "y":
        start_game()
    else:
        sys.exit("\nGame Over!\n")


def start_game():

    options = "\nEnter...\n1 for Rock,\n2 for Paper,\n3 for Scissor:\n\n"
    print(options)

    playerChoice = input("Select between 1 - 3 : ")

    valid_choice(playerChoice)

    player = int(playerChoice)

    computerChoice = random.choice("123")

    computer = int(computerChoice)

    print("\nYou chose: " + options_chosen(player))
    print("\nPython chose: " + options_chosen(computer))

    who_won(player, computer)

    print("\n--------------------")

    game_restart()


start_game()
