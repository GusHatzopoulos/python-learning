from random import randint

choices = ["rock", "paper", "scissors"]

while True:
    print("----------------------------------")
    print("...Rock...")
    print("...Paper...")
    print("...Scissors...")

    player = input("Player, make your choice: ").lower()
    if player in ("quit", "exit", "q"):
        print("Thanks for playing!")
        break
    if player not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    
    computer = choices[randint(0,2)]

    print(f"\n************")
    print(f"Player chose: {player}")
    print(f"Computer chose: {computer}")
    print(f"************\n")

    if player == computer:
        print("Its a tie!")
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
         print("Player wins the round!")
    else:
    #     print("Computer wins the round!")

print("----------------------------------")