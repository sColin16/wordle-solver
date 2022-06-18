'''
This file contains all the utilities for searching the word space, simulating
the game, and more
'''

import random

from collections import defaultdict, Counter
from statistics import mean
from typing import Callable, Dict, Set, Tuple
from tqdm import tqdm

def load_words() -> Tuple[Set[str], Set[str]]:
    '''
    Returns the set of all valid words for guesses, and the subset of valid
    words that are valid solutions, based on a dataset from Kaggle
    '''

    # Strip out the header from both tables
    with open('data/valid_guesses.csv', 'r',) as f:
        guesses = set(line.strip() for i, line in enumerate(f) if i > 0)

    with open('data/valid_solutions.csv', 'r',) as f:
        solutions = set(line.strip() for i, line in enumerate(f) if i > 0)

    valid = guesses.union(solutions)

    return valid, solutions

def choose_word(solutions: Set[str]) -> str:
    '''
    Chooses a random word from a set of possible solutions
    '''

    return random.choice(list(solutions))

def generate_hint(guess: str, sol: str) -> Tuple[int, int, int, int, int]:
    '''
    Determines the yellow/green/grey hint for a guess, given a solution

    0 is for grey, 1 is for yellow, 2 is for green
    '''

    hint = [0] * 5
    sol_count = Counter(sol)

    # Apply the green hints
    for i in range(5):
        if sol[i] == guess[i]:
            hint[i] = 2
            sol_count[sol[i]] -= 1

    # Apply the yellow hints
    for i in range(5):
        if sol_count[guess[i]] > 0 and hint[i] != 2:
            hint[i] = 1
            sol_count[guess[i]] -= 1

    return tuple(hint)

def find_subset(guess:str, hint: Tuple[int, int, int, int, int], solutions: Set[str]) -> Set[str]:
    '''
    Reduces the number of possible solutions given a hint from a guess
    '''

    output = set()

    for sol in solutions:
        if generate_hint(guess, sol) == hint:
            output.add(sol)

    return output

def get_dist(valid: Set[str], solutions: Set[str]) -> Dict[str, Set[int]]:
    '''
    Determines the distribution of remaining possible words for guessing each
    word in a set of valid guesses, given the set of possible solution words
    '''

    full_dist = {}

    for word in tqdm(valid):
        counts = defaultdict(int)

        for sol in solutions:
            hint = generate_hint(word, sol)

            counts[hint] += 1

        full_dist[word] = counts

    return {word: set(value.values()) for word, value in full_dist.items()}

def summarize_dist(dist: Dict[str, Set[int]],
        transform: Callable[[Set[int]], int]) -> Dict[str, int]:
    '''
    General function for summarizing a distribution of remaining words when a
    given word is guessed. The resulting dictionary is sorted
    '''

    summary_list = sorted((transform(value), word) for word, value in dist.items())

    return dict(map(lambda x: (x[1], x[0]), summary_list))

def get_mean_dist(dist: Dict[str, Set[int]]) -> Dict[str, int]:
    '''
    Returns the expected value of the number of words remaining for each word
    '''

    return summarize_dist(dist, mean)

def get_max_dist(dist: Dict[str, Set[int]]) -> Dict[str, int]:
    '''
    Returns the maximum number of words remaining for each word
    '''

    return summarize_dist(dist, max)
