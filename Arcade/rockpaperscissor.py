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


def rock_paper_scissor(name="PlayerO"):

    game_count = 0
    player_wins = 0
    python_wins = 0

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

    def game_restart():
        restart = input(
            "\nPlay Again? \n\npress 'Y' If not press 'Q' to quit : ")

        if restart.lower() not in ["y", "q"]:
            print("\nChoose 'Y' to play or 'Q' to quit")
            game_restart()

        while restart.lower() == "y":
            start_game()
        else:
            if (__name__ == "__main__"):
                sys.exit("\nGame Over!\n")
            else:
                return

    def who_won(player, computer):
        nonlocal player_wins
        nonlocal python_wins
        if player == computer:
            tie()
        elif player == 1 and computer == 3:
            player_wins += 1
            user_won()
        elif player == 2 and computer == 1:
            player_wins += 1
            user_won()
        elif player == 3 and computer == 2:
            player_wins += 1
            user_won()
        else:
            python_wins += 1
            python_won()

    def start_game():

        nonlocal game_count
        nonlocal name

        options = f"\n{name}, Please enter...\n1 for Rock,\n2 for Paper,\n3 for Scissor:\n\n"
        print(options)

        playerChoice = input("Select between 1 - 3 : ")

        valid_choice(playerChoice)

        player = int(playerChoice)

        computerChoice = random.choice("123")

        computer = int(computerChoice)

        print(f"\nYou chose: {options_chosen(player)}")
        print(f"\nPython chose: {options_chosen(computer)}")

        game_count += 1
        who_won(player, computer)

        print(f"\n Games Played : {game_count}")
        print(f"\n Player Won : {player_wins}")
        print(f"\n Python Won : {python_wins}")

        print("\n--------------------")

        game_restart()

    return start_game


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game"
    )

    args = parser.parse_args()

    play = rock_paper_scissor(args.name)
    play()
