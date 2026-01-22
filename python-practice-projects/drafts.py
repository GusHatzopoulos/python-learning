from random import randint

choices = ["rock", "paper", "scissors"]

while True:

    print("----------------------------------")
    print("...Rock...\n...Paper...\n...Scissors...")
    # print("...Paper...")
    # print("...Scissors...")
    print("SHOOT!")

    player = input('Player, make your choice between rock, paper, or scissors\n" \
        "or type "quit", "exit" or "q", to quit the gane: ').lower()
    print("***NO CHEATING! GAME STARTED!***\n" * 6)
    if player in("quit", "exit", "q"):
        print("Quiting game. Thanks for playing!")
        break
    if player not in choices:
        print("Invalid choice. Choose between rock, paper, or scissors.")
        continue

    computer = choices[randint(0,2)]

    print(f"\n************")
    print(f"Player chose {player}.")
    print(f"Computer chose {computer}.")
    print(f"\n************")

    if player not in choices or computer not in choices:
        print('Invalid input. Choose between "rock", "paper", "scissors".')
    elif player == computer:
        print("Its a tie!")
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("Player wins the round!")
    else:
        print("Computer wins the round!")
print("----------------------------------")