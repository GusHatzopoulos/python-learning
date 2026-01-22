print("...Rock...")
print("...Paper...")
print("...Scissors...")

player1 = input(str("Player 1, make your move: ")).lower()
player2 = input(str("Player 2, make your move: ")).lower()

if player1 == player2:
    print("Its a tie!")
elif player1 == "rock":
    if player2 == "scissors":
        print("Player 1 wins!")
    elif player2 == "paper":
        print("Player 2 wins!")
elif player2 == "rock":
    if player1 == "paper":
        print("Player 1 wins!")
    elif player1 == "scissors":
        print("Player 1 wins!")

print("SHOOT!")