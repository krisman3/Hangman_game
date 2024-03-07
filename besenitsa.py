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


def noose_count(count):
    scaffold = [
        "--------",
        "|      |",
        "|      ",
        "|      ",
        "|      ",
        "|      ",
        "========"
    ]
    if count > 0:
        scaffold[2] = "|      O"
    if count > 1:
        scaffold[3] = "|      |"
    if count > 2:
        scaffold[3] = "|     /|"
    if count > 3:
        scaffold[3] = "|     /|\\"
    if count > 4:
        scaffold[4] = "|     /"
    if count > 5:
        scaffold[4] = "|     / \\"
    for line in scaffold:
        print(line)


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

# Allowing the second player to set a word.
word_to_guess = random_word()
# Show the empty board
board = print_board(word_to_guess)
# Initializing the count
count = global_count()

while True:

    # The player starts guessing
    guess = player_guess()

    # Performing a check and printing the appropriate message
    check = check_guess(board, word_to_guess, guess, count)
    if check == 'Congratulations! You survived.':
        print(check)
        break
    elif check == "You've been hung.":
        print(check)
        print("The word was:", word_to_guess)
        break
    print_board(board)
    noose_count(count)

