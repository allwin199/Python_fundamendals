import sys
import random

def startGame():

    options = "\nEnter...\n1 for Rock,\n2 for Paper,\n3 for Scissor:\n\n"
    print(options)

    playerChoice = input("Select between 1 - 3 : " )

    player = int(playerChoice)

    if player < 1 or player > 3:
        sys.exit("Invalid Input")

    computerChoice = random.choice("123")

    computer = int(computerChoice)

    def optionsChosen(val):
        if val == 1:
            return "Rock"
        elif val == 2:
            return "Paper"
        elif val == 3:
            return "Scissors"

    print("\nYou chose: " + optionsChosen(player))
    print("\nPython chose: " + optionsChosen(computer))

    def userWon():
        print("\n🎉 You Won!")

    def pythonWon():
        print("\n🐍 Python Won!")

    def tie():
        print("\n👍 Tie!")


    if player == computer : 
        tie()
    elif player == 1 and computer == 3:
        userWon()
    elif player == 2 and computer == 1: 
        userWon()
    elif player == 3 and computer == 2:
        userWon()
    else:
        pythonWon()


    print("\n--------------------")
    restart = input("\nPlay Again? \n\npress 'Y' If not press  'N' : ")
        
    while restart.lower() == "y":
        startGame()
    else:
        sys.exit("\nGame Over!\n")

    
startGame()



