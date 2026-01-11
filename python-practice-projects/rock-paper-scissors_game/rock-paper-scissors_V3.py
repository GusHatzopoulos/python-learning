print("...Rock...")
print("...Paper...")
print("...Scissors...")

player1 = input("(enter Player 1's choice): ").lower()
player2 = input("(enter Player 2's choice): ").lower()

if player1 == player2:
    print("Its a tie!")

    print("Player 1 wins!")
else:
    print("Player 2 wins!")

print("SHOOT!")