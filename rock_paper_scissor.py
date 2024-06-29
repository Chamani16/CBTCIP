#we need to import random module 
import random
while(1):
    user_input = input("Enter a choice :")
    options = ["rock","paper","scissors"]
    computer_input = random.choice(options)
    print("you chose:" user_input)
    print("computer chose:" computer_input)
    if user_input == computer_input:
        print("It's a tie")
    elif user_input == "rock":
        if computer_input == "scissors":
            print("Rock wins")
        else:
            print("Paper wins")
    elif user_input == "paper":
        if computer_input == "rock":
            print("paper wins")
        else:
            print("Scissors wins")
    elif user_input == "scissors":
        if computer_input == "paper":
            print("Scissors wins")
        else:
            print("Rock wins")
    play_again = input("Do you want to play again? (Y/N):")
    if play_again == "N":
        break
     
