'''
This is an interactive wordle solver that can be run while playing wordle to
identify good guesses

Enter your guess in lowercase, and use X, Y, and G to denote grey, yellow, and
green hints from wordle

Example:
GUESS> trace
HINT>  YXXXY
'''

from statistics import mean
from utils import load_words, find_subset, get_dist, get_mean_dist, get_max_dist

HINT_MAP = {'X': 0, 'Y': 1, 'G': 2}
SUGGESTIONS = 5

valid, curr_solutions = load_words()

with open('data/mean_dist_initial.txt', 'r') as f:
    curr_mean_dist = eval(f.readline())

with open('data/max_dist_initial.txt', 'r') as f:
    curr_max_dist = eval(f.readline())

for i in range(6):
    print(f'{len(curr_solutions)} possible words left')

    if len(curr_solutions) > 1:
        print('BEST EXPECTED REMAINING')
        for entry in list(curr_mean_dist.items())[:SUGGESTIONS]:
            print(*entry)

        print('BEST WORST CASE REMAINING')
        for entry in list(curr_max_dist.items())[:SUGGESTIONS]:
            print(*entry)

    else:
        print('SOLUTION')
        print(list(curr_solutions)[0])
        break

    guess = input('GUESS> ')
    hint = input('HINT>  ')
    hint = tuple(map(lambda x: HINT_MAP[x], hint))

    curr_solutions = find_subset(guess, hint, curr_solutions)

    new_dist = get_dist(curr_solutions, curr_solutions)
    curr_mean_dist = get_mean_dist(new_dist)
    curr_max_dist = get_max_dist(new_dist)
