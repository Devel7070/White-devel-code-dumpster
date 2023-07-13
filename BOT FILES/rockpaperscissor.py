# Welcome
import random
import time


def game():

    print("Welcome to RPS Simulator.")
    time.sleep(2)
    # Input - Either Rock, Paper, or Scissors.
    user_choice = input(str("Enter your choice: "))
    print("Calculating my choice")
    time.sleep(3)
    # Generate Objcet.
    # Taking a number from a list:
    number = ["rock", "paper", "scissor"]
    number = random.choice(number)
    if number == "rock":
        print("I choose Rock.")
    elif number == "paper":
        print("I choose Paper.")
    elif number == "scissor":
        print("I choose Scissor.")
    time.sleep(2)
    # Seeing who has won.
    # DRAW:
    if user_choice == number:
        print("Thats a draw!")
    # AI WINS:
    if user_choice == "rock" and number == "paper":
        print("Haha I win!")
    elif user_choice == "paper" and number == "scissor":
        print("Haha I win!")
    elif user_choice == "scissor" and number == "rock":
        print("Haha I win!")
    # PLAYER WINS:
    if user_choice == "rock" and number == "scissor":
        print("I lost!")
    elif user_choice == "scissor" and number == "paper":
        print("I lost!")
    elif user_choice == "paper" and number == "rock":
        print("I lost!")

    restart = input("Do you want to restart? (yes/no)")
    while restart.lower() not in ["yes", "no"]:
        print("Enter a yes or a no")
        time.sleep(1.5)
        restart = input("rematch or no rematch (yes/no)")
    if restart == "yes":
        game()


game()
