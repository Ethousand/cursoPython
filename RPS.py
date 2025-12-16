import random

Player = input('Enter your choice R for rock, P for paper, S for scissors: ').upper()
Computer = random.choice(['R', 'P', 'S'])

# Dictionary for showing full names
RPS = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

# Validate player input
while Player not in ['R', 'P', 'S']:
    Player = input('Invalid input! Please enter R for rock, P for paper, S for scissors: ').upper()

# Im gonna use logic staments for to simplify the logic of the game
# first its tie, second player win, last computer win
if Player == Computer:
    print(f'Both chose {Player}. It\'s a tie!')
elif (Player == 'R' and Computer == 'S') or \
     (Player == 'P' and Computer == 'R') or \
     (Player == 'S' and Computer == 'P'):
        print(f"Player wins! {RPS[Player]} beats {RPS[Computer]}")
else:
    print("Computer wins!", f"{RPS[Computer]} beats {RPS[Player]}")