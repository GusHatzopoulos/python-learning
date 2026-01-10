print("...Rock...")
print("...Paper...")
print("...Scissors...")

player1 = input("(enter Player 1's choice): ")
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