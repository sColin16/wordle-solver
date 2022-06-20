# Wordle Solver

An interactive Wordle solver that provides tips for quickly finding the solution
to the daily Wordle.

## Structure
- solve.py is the interactive solver that allows you to input your guess and the
  hint that results, while providing suggestions for words to guess next that
  will cut down the number of possible words quickly.
- sim.py is a Worlde simulator
- initial.py generates the data for the optimal first word to guess
- utils.py contains various utility functions used across all the scripts
- data contains the Wordle dictionaries, and precomputed data for choosing an
  initial word (which takes a while to compute)

## Current Approach

The current approach is a brute force search across all valid guesses and
solutions. For every word that could be guessed, we consider every word that
could be solution, and analyze the distribution of the number of possible
remaining words after guessing each word. We suggest words with the lowest mean
number of words remaining (or lowest max number of words remaining)

## Future Improvements

The current approach only searches at a depth of one, considering only the next
word. Ideally, the search would be complete, determining the expected number of
guesses that would be needed for each word that could be guessed. This is more
complicated and probably only offers a marginal improvement in practice.

Alternatively, the current algorithm could be used to make a coach that rates
the strength of guesses and offers suggestions for better or alternative
guesses to help improve play.
