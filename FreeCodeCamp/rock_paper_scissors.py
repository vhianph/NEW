import random

def play():
    player = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors: ")
    computer = random.choice(['r', 'p', 's'])
    
    print(f"Computer chose: {computer}")
    
    if player == computer:
        print("Draw!")
    elif is_win(player, computer):
        print("You won!")
    else:
        print("You lose!")

def is_win(player, computer):
    # Return True if the player beats the computer
    # Winning conditions: r > s, s > p, p > r
    return (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r')

if __name__ == "__main__":
    play()
