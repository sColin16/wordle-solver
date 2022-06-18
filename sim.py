'''
This is a simulation of wordle. After entering a guess, it shows X, Y, and G
for each letter to indicate grey, yellow, and green, respectively
'''

from utils import load_words, choose_word, generate_hint, find_subset, get_dist
from statistics import mean

HINT_MAP = {0: 'X', 1: 'Y', 2: 'G'}

valid, solutions = load_words()
solution = choose_word(solutions)
# print('SOLUTION', solution)

for i in range(6):
    guess = input('GUESS> ')
    
    hint = generate_hint(guess, solution)

    print(' ' * 6, ''.join(map(lambda x: HINT_MAP[x], hint)))

    if hint == (2, 2, 2, 2, 2):
        print(f'SOLVED in {i + 1} guesses')
        break

if hint != (2, 2, 2, 2, 2):
    print('FAILED')
