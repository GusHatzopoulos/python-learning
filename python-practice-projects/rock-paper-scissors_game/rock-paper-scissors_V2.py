print("...Rock...")
print("...Paper...")
print("...Scissors...")

player1 = input("(enter Player 1's choice): ").lower()
print("***NO CHEATING! GAME STARTED!***\n" * 30)
player2 = input("(enter Player 2's choice): ").lower()

if player1 == player2:
    print("Its a tie!")
elif player1 == "rock":
    if player2 == "scissors":
        print("Player 1, wins!")
    elif player2 == "paper":
        print("Player 1, wins!")
elif player1 == "paper":
    if player2 == "rock":
        print("Player 1, wins!")
    elif player2 == "scissors":
        print("Player 2, wins!")
elif player1 == "scissors":
    if player2 == "paper":
        print("Player 1, wins!")
    elif player2 == "rock":
        print("Player 2, wins!")
else:
    print("Something went wrong.")
        
print("SHOOT!")