import random
from random import choice

# Setting a random word to guess
word = ''
def global_count():
    return 0
def random_word():
    global word
    categories = ["biology", "geography", "entertainment", "sports"]
    category = random.choice(categories)
    word = input(f"Choose a word from category {category}: ")
    return word.lower()


def print_board(pulled_word):
    length = len(pulled_word)
    return "_" * length


def player_guess():
    guess_letter = input("Guess an existing letter: ")
    return guess_letter.lower()


def noose_count(count):  # I'll use the global_count method for this one
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


# Once again - will use the global_count method
def check_guess(board: list, actual_word: str, player_letter: chr, count):
    print(board)
    if player_letter in actual_word:
        for i in range(len(actual_word)):
            if player_letter == actual_word[i]:
                board[i] = player_letter
                continue
    elif ''.join(board) == actual_word:
        count = 0
        return 'Congratulations! You survived.'

    else:
        count += 1
        if count < 8:
            return "Keep guessing..."
        else:
            return "You've been hung."


# Main logic of the game:
word_to_guess = random_word()

