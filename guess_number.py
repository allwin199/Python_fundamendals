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


def game_restart():
    restart = input("\nPlay Again? \n\npress 'Y' If not press 'Q' to quit : ")

    if restart.lower() not in ["y", "q"]:
        print("\nChoose 'Y' to play or 'Q' to quit")
        game_restart()

    while restart.lower() == "y":
        start_game()
    else:
        sys.exit("\nGame Over!\n")


def calculate_percentage(games_played, games_won):
    return round((games_won/games_played)*100, 2)


def guess_number(name="PlayerO"):

    game_count = 0
    player_wins = 0
    python_wins = 0

    def valid_choice(player):
        if player not in ["1", "2", "3"]:
            print("\nYou must enter 1,2 or 3")
            start_game()
        else:
            return

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
            sys.exit("\nGame Over!\n")

    def who_won(player, computer):
        nonlocal player_wins
        nonlocal python_wins
        if player == computer:
            player_wins += 1
            user_won()
        else:
            python_wins += 1
            python_won()

    def start_game():

        nonlocal game_count
        nonlocal name

        options = f"\n{name}, Please guess which number I am thinking between 1,2 and 3...\n"
        print(options)

        playerChoice = input("Select between 1 - 3 : ")

        valid_choice(playerChoice)

        player = int(playerChoice)

        computerChoice = random.choice("123")

        computer = int(computerChoice)

        print(f"\nYour Answer: {player}")
        print(f"\nPython's Answer: {computer}")

        game_count += 1
        who_won(player, computer)

        print(f"\n Games Played : {game_count}")
        print(f"\n Player Won : {player_wins}")
        print(f"\n Python Won : {python_wins}")

        print(
            f"\n Player Winning Percentage : {calculate_percentage(game_count, player_wins)}")

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

    play = guess_number(args.name)
    play()
