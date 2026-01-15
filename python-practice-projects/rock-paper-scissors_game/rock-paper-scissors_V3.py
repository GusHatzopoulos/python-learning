print("...Rock...")
print("...Paper...")
print("...Scissors...")

player1 = input("(enter Player 1's choice): ").lower()
print("***NO CHEATING! GAME STARTED!***\n" * 10)
player2 = input("(enter Player 2's choice): ").lower()

if player1 == player2:
    print("Its a tie!")
elif (
    (player1 == "rock" and player2 == "scissors") or
    (player1 == "paper" and  player2 == "rock") or
    (player1 == "scissors" and player2 == "paper")
):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")


# if player1 == player2:
#     print("Its a tie!")
# elif (
#     (player1 == "rock" and player2 == "scissors") or
#     (player1 == "paper" and player2 == "rock") or
#     (player1 == "scissors" and player2 == "paper")
# ):
#     print("Player 1 wins!")
# else:
#     print("Player 2 wins!")

print("SHOOT!")