'''
This file computes and saves distributions for the number of valid solution
words remaining for each possible first word. It computes the mean and max of
these distributions for each word
'''

from utils import load_words, get_dist, get_mean_dist, get_max_dist

valid, solutions = load_words()

dist = get_dist(valid, solutions)
mean_dist = get_mean_dist(dist)
max_dist = get_max_dist(dist)

with open('data/dist_initial.txt', 'w') as f:
    f.write(str(dist))

with open('data/mean_dist_initial.txt', 'w') as f:
    f.write(str(mean_dist))

with open('data/max_dist_initial.txt', 'w') as f:
    f.write(str(max_dist))
