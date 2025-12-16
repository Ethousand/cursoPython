import random
Player = input('Enter your choice R for rock, P for paper, S for scissors: ').upper()


while Player not in ['R', 'P', 'S']:
    Player = input('Invalid input! Please enter R for rock, P for paper, S for scissors: ').upper()

Computer = random.choice(['R', 'P', 'S'])

if Player == 'R':
    if Computer == 'S':
        print("Player wins! Rock crushes Scissors.")
    elif Computer == 'R':
        print("It's a tie! Both chose Rock.")

elif Player == 'P':
    if Computer == 'R':
        print("Player wins! Paper covers Rock.")
    elif Computer == 'P':
        print("It's a tie! Both chose Paper.")

elif Player == 'S':
    if Computer == 'P':
        print("Player wins! Scissors cut Paper.")
    elif Computer == 'S':
        print("It's a tie! Both chose Scissors.")
else:
    


Computer = random.choice(['R', 'P', 'S'])


print(f"Player: {Player}, Computer: {Computer}")