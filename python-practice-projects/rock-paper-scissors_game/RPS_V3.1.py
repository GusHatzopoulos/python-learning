from random import choice

choices = ["rock", "paper", "scissors"]
wins_against = {"rock": "scissors", "paper": "rock", "scissors": "rock"}
quit_cmds = ["quit", "exit", "q"]

while True:
    print("----------------------------------")
    print("...Rock...\n...Paper...\n...Scissors...")
    print("SHOOT!")

    player = input(
        'Player, make your choice between "rock", "paper", or "scissors",\n' \
        'or type "quit", "exit" or "q", to quit the game: '
    ).lower()

    if player in(quit_cmds):
        print("Quiting game. Thanks for playing!")
        break
    if player not in(choices):
        print("Invalid choice. Choose between rock, paper, or scissors.")
        continue

    print("***NO CHEATING!***\n" * 6)

    print(f"[DEBUG] player = {player!r}.")

    print("----------------------------------")