print("...Rock...")
print("...Paper...")
print("...Scissors...")

player1 = input("(enter Player 1's choice): ")
print("***NO CHEATING! GAME STARTED!***\n" * 20)
player2 = input("(enter Player 2's choice): ")

if player1 == player2:
    print("Its a tie!")
elif player1 == "rock":
    if player2 == "scissors":
        print("Player1 wins!")
    elif player2 == "paper":
        print("Player 1 wins!")
elif player1 == "paper":
    if player2 == "rock":
        print("Player1 wins!")
    elif player2 == "scissors":
        print("Player2 wins!")
elif player1 == "scissors":
    if player2 == "paper":
        print("Player2 wins!")
    elif player2 == "rock":
        print("Player2 wins!")
else:
    print("Something went wrong.")

print("SHOOT!")