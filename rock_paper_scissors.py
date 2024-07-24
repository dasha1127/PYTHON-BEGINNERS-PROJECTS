import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        comp_choice = random.choice(choices)
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to stop playing): ").lower()

        if player_choice == 'quit':
            print("Thanks for playing!")
            break

        if player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        print(f"Computer chose {comp_choice}.")

        if player_choice == comp_choice:
            print(f"Both players selected {player_choice}. It's a tie!")
        elif (player_choice == 'rock' and comp_choice == 'scissors') or \
             (player_choice == 'paper' and comp_choice == 'rock') or \
             (player_choice == 'scissors' and comp_choice == 'paper'):
            print("You win!")
        else:
            print("Computer wins!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

play_game()
