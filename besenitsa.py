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


def noose_count(count):
    if count == 0:
        print("--------")
    elif count == 1:
        print("--------"
              "   O    ")
    elif count == 2:
        print("--------"
              "   O    "
              "   |    ")
    elif count == 3:
        print("--------"
              "   O    "
              "   |    "
              "  /     ")
    elif count == 4:
        print("--------"
              "   O    "
              "   |    "
              "  / \   ")
    elif count == 5:
        print("--------"
              "   O    "
              "  /|    "
              "  / \   ")
    elif count == 6:
        print("--------"
              "   O    "
              "  /|\   "
              "  / \   ")
    elif count == 7:
        print("--------"
              "   O_    "
              "  /|\   "
              "  / \   ")
    elif count == 8:
        print("--------"
              "   O_|    "
              "  /|\   "
              "  / \   ")


def check_guess(board: list, actual_word: str, player_letter: chr):
    print(board)
    if player_letter in actual_word:
        for i in range(len(actual_word)-1):
            if player_letter == actual_word[i]:
                board[i] = player_letter
                continue
    elif board == actual_word:
        return 'Congratulations! You survived.'
    else:



    return ''.join(board)

