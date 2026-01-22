from random import randint

print("...Rock...")
print("...Paper...")
print("...Scissors...")

choices = ["rock", "paper", "scissors"]

player = input("(enter Player 1's choice): ").lower()
print("***NO CHEATING! GAME STARTED!***\n" * 10)
computer = input("(enter Player 2's choice): ").lower()

if player not in choices or computer not in choices:
    print('Invalid input. Choose between "rock", "paper", "scissors".')
elif player == computer:
    print("Its a tie!")
elif (
    (player == "rock" and computer == "scissors") or
    (player == "paper" and computer == "rock") or
    (player == "scissors" and computer == "paper")
):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")

print("SHOOT!")