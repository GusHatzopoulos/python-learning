from random import randint

print("...Rock...")
print("...Paper...")
print("...Scissors...")

choices = ["rock", "paper", "scissors"]

player = input('Player, make your choice between rock, paper, or scissors\n" \
    "or type "quit", "exit" or "q", to quit the gane: ').lower()
print("***NO CHEATING! GAME STARTED!***\n" * 10)
computer = choices[randint(0,2)]

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
    print("Computer wins!")

print("SHOOT!")