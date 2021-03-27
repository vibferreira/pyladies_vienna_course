from random import randrange

#it selects any number from 0 to 2
number = randrange(2)

#initiating the variable before the loop
pc_choice = ""
if number == 0:
    pc_choice = "rock" 
elif number == 1:
    pc_choice = "paper"
else:
    pc_choice = "scissors"

#user input
user_choice = input("input a rock, paper or scissor: ")

#iterate troughout the possibilities
if pc_choice == "rock" and user_choice == "rock":
    print("The computer chose", pc_choice, "it is a draw!")
elif pc_choice == "rock" and user_choice == "paper":
    print("The computer chose", pc_choice, "you won!")
elif pc_choice == "rock" and user_choice == "scissor":
    print("The computer chose", pc_choice, "you lost!")
elif pc_choice == "paper" and user_choice == "paper":
    print("The computer chose", pc_choice, "it is a draw!")
elif pc_choice == "paper" and user_choice == "scissor":
    print("The computer chose", pc_choice, "you won!")
elif pc_choice == "paper" and user_choice == "rock":
    print("The computer chose", pc_choice, "you lost!")
elif pc_choice == "scissors" and user_choice == "scissor":
    print("The computer chose", pc_choice, "it is a draw!")
elif pc_choice == "scissors" and user_choice == "rock":
    print("The computer chose", pc_choice, "you won!")
elif pc_choice == "scissors" and user_choice == "paper":
    print("The computer chose", pc_choice, "you lost!")