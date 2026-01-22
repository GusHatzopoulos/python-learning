print("...Rock...")
print("...Paper...")
print("...Scissors...")

player1 = input("Player 1 make your choice: ").lower()
player2 = input("Player 2 make your choice: ").lower()

choices = ["rock", "paper", "scissors"]
if player1 not in choices or player2 not in choices:
    print('Invalid/wrong input. Choose between "rock", "paper", "scissors".')
elif player1 == player2:
    print("Its a tie!")
elif player1 == "rock" and player2 == "scissors":
    print("Player 1 wins!")
elif player1 == "paper" and player2 == "rock":
    print("Player 1 wins!")
elif player1 == "scissors" and player2 == "paper":
    print("Player 1 wins!")
else:
    print("PLayer 2 wins!")

# player1 = input("Player 1, make your move: ").lower()
# player2 = input("Player 2, make your move: ").lower()

# choices = ["rock", "paper", "scissors"]
# if player1 not in choices or player2 not in choices:
#       print('"Invalid/wrong input. Choose between "rock", "paper", "scissors".')

# elif player1 == player2:
#     print("Its a tie!")
# elif player1 == "rock" and player2 == "scissors":
#         print("Player 1 wins!")
# elif player1 == "paper" and player2 == "rock":
#         print("Player 1 wins!")
# elif player1 == "scissors" and player2 == "paper":
#         print("Player 1 wins!")
# else:
#     print("Player 2 wins!")         

print("SHOOT!")