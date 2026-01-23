from random import choice

choices = ["rock", "paper", "scissors"]
wins_against = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
quit_cmds = ["quit", "exit", "q"]

while True:

    print("----------------------------------")
    print("...Rock...\n...Paper...\n...Scissors...")
    print("SHOOT!")

    player = input(
        'Player, make your choice between "rock", "paper", or "scissors",\n' \
        'or type "quit", "exit" or "q", to quit the game: '
        ).lower()
    
    print("***NO CHEATING! GAME STARTED!***\n" * 6)

    if player in(quit_cmds):
        print("Quitting game. Thanks for playing!")
        break
    if player not in choices:
        print("Invalid choice. Choose between rock, paper, or scissors.")
        continue

    computer = choice(choices)

    print(f"\n************")
    print(f"Player chose {player}.")
    print(f"Computer chose {computer}.")
    print(f"\n************")

    if player == computer:
        print("Its a tie!")
    elif wins_against[player] == computer:
        print("Player wins the round!")
    else:
        print("Computer wins the round!")
        
print("----------------------------------")