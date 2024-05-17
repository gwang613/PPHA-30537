# Qiuzhi (George) Wang

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

import random

choices = ['rock', 'paper', 'scissors']

# def get_player_choice():
#     return input('Pick one of rock, paper, or scissors: ').lower()

# def get_computer_choice():
#     return random.choice(choices)

# def determine_winner(p1, p2):
#     if p1 == p2:
#         return 'Tie'
#     elif (p1 == 'rock' and p2 == 'scissors') or \
#          (p1 == 'paper' and p2 == 'rock') or \
#          (p1 == 'scissors' and p2 == 'paper'):
#         return 'Win'
#     else:
#         return 'Lose'

# def num_play():
#     return int(input('Pick the number of human player (from 0 to 2).'))

# def game():
#     win = 0
#     loss = 0
#     continue_game = 1

#     while continue_game == 1:
#         if num_play == 1:
#             p1 = get_player_choice()
#             p2 = get_computer_choice()
#             print(f"Computer picked: {p2}")
#         if num_play == 2:
#             p1 = get_player_choice()
#             p2 = get_player_choice()
#             print(f"P1 picked: {p1}")
#             print(f"P2 picked: {p2}")
        
#         result = determine_winner(p1, p2)
        
#         if result == 'Tie':
#             print('It\'s a Tie.')
#         elif result == 'Win':
#             win += 1
#             print('You win.')
#         else:
#             loss += 1
#             print('You lose.')

#         print(f"Score - Wins: {win}, Losses: {loss}")
#         continue_game = int(input('Continue? (1: Yes, 0: No): '))
    

# if __name__ == "__main__":
#     game()


beats = {'rock': 'scissors', 'paper':'rock', 'scissors':'paper'}

p1 = random.choice(choices)
p2 = random.choice(choices)

def find_winner(p1, p2):
    if beats[p1] == p2:
        return 'P1 wins.'
    elif beats[p2] == p1:
        return 'P2 wins.'
    else:
        return 'Tie.'
    
def randomize():
    return random.choice(choices)

def player_input():
    return input('Choose rock, paper, scissors')

def play_once():
    p1 = randomize()
    p2 = randomize()
    print(f'Player 1: {p1}\nPlaer2: {p2}')

    winner = find_winner(p1, p2)
    print(f'Winner is : {winner}')

play_once()








