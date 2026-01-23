from random import choices

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
    
    




    print("----------------------------------")