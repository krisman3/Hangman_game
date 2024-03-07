import random
from random import choice

# Setting a random word to guess
word = ''

def random_word():
    global word
    lst_of_words = []
    word = random.choice(lst_of_words)
    return word


def print_board(pulled_word):
    length = len(pulled_word)
    return "_" * length


def player_guess():
    guess_letter = input("Guess an existing letter: ")
    return guess_letter


def check_guess(board: str, actual_word: str, player_letter: chr):
    print(board)

    for i in actual_word:
        if player_letter in actual_word:
            ind = actual_word.index(player_letter)
