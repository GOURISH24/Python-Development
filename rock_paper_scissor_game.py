
import random

print("Welcome to Rock, Paper, Scissor!")
print("Best of 5 will win the game.")

choices = ["rock", "paper", "scissor"]
def get_computer_choice():
    return random.choice(choices)

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissor): ").lower().strip()
        if user_choice in choices:
            return user_choice
        elif user_choice == "":
            print("You didn't enter anything. Please enter rock, paper, or scissor.")
        else:
            print("Invalid input. Please enter rock, paper, or scissor.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        
        return "player"
    else:
        
        return "computer"

def play_game():
    
    user_hand = get_user_choice()
    computer_hand = get_computer_choice()
    print(f"You chose: {user_hand}")
    print(f"The computer chose: {computer_hand}")
    return determine_winner(user_hand, computer_hand)
    

# Start the game

while True:
    player_score = 0
    comp_score = 0
    for i in range (1,6):
        print(f"\nRound: {i}")
        winner = play_game()
        if winner == "player":
            player_score += 1
            print("You won this round!")
        elif winner == "computer":
            comp_score += 1
            print("You lost this round!")
        else:
            print("It's a tie!")
        i=i+1
    if player_score > comp_score:
        print(f"\nYou won the Game, your score: {player_score}, computer score: {comp_score}")
    elif player_score == comp_score:
        print(f"\nThis Game was a tie, your score: {player_score}, computer score: {comp_score}")
        
    else:
        print(f"\nYou lost the Game, your scores: {player_score}, computer score: {comp_score}")
    
    play_again = input("\nDo you want to play again? (yes or no): ").lower().strip()
    
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("\nWelcome to New Game.\n")


