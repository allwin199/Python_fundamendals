import sys
import rockpaperscissor
import guess_number


def choose_game(name="Player0"):

    welcome_back = False

    while True:
        if welcome_back == True:
            print("\nWelcome Back to Arcade menu!")

        options = f"\n{name}, Select which game you want to play...\n\n1 for Rock Paper Scissor\n2 for Guess Number \nx to quit"
        print(options)

        playerChoice = input("\nSelect 1, 2 or x : ")

        if (playerChoice not in ["1", "2", "x"]):
            print("\nYou must enter 1,2 or x")
            return choose_game(name)

        welcome_back = True

        if (playerChoice == "1"):
            play = rockpaperscissor.rock_paper_scissor(name)
            play()
        elif (playerChoice == "2"):
            play = guess_number.guess_number(name)
            play()
        else:
            sys.exit("\nThanks!")


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

    choose_game(args.name)
