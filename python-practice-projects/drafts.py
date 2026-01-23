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
    
    print("***NO CHEATING!***\n * 6")

    if player in(quit_cmds):
        print("Quiting game. Thanks for playing!")
        break
    if player not in(choices):
        print("Invalid choice. Choose between rock, paper, or scissors.")
        continue
    




    print("----------------------------------")