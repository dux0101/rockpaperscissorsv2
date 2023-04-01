import random


options = ["rock", "paper", "scissors"]


user_choice = input("Choose rock, paper or scissors: ".lower())

computer_choice = random.choice(options)

print("You Chose:", user_choice)
print("The Computer Chose", computer_choice)

if user_choice == computer_choice:
    print("Its a tie")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You Win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You Win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You Win!")
else:
    print("The Computer Wins!")
