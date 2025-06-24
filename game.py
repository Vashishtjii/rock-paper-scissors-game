import random
def play_game():
    # Game setup
    choices = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0
    
    print("\nWelcome to Rock-Paper-Scissors!")
    print("Best of 3 wins. Type 'quit' to exit.\n")
    
    while True:
        # Show score
        print(f"Score - You: {player_score} | Computer: {computer_score}")
        
        # Player choice
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        
        # Exit condition
        if player_choice == 'quit':
            print("\nThanks for playing!")
            if player_score > computer_score:
                print(f"You won {player_score}-{computer_score}!")
            elif computer_score > player_score:
                print(f"Computer won {computer_score}-{player_score}.")
            else:print("It was a tie game!")
            break
            
        # Validate input
        if player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
            
        # Computer choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (
            (player_choice == 'rock' and computer_choice == 'scissors') or
            (player_choice == 'paper' and computer_choice == 'rock') or
            (player_choice == 'scissors' and computer_choice == 'paper')
        ):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
            
        # Check for game winner
        if player_score == 2 or computer_score == 2:
            if player_score > computer_score:
                print("\nCongratulations! You won the game!")
            else:
                print("\nComputer won the game!")
            print(f"Final Score - You: {player_score} | Computer: {computer_score}")
            another_game = input("Play again? (yes/no): ").lower()
            if another_game == 'yes':
                play_game()
            else:
                print("Thanks for playing!")
            break
            
if __name__ == "__main__":
    play_game()
