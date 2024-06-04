# Imports
import random
import time

# Lives
lives = 5

words = ["apple", "pizza", "mario", "teeth", "shirt", "lives", "linus", "guess", "music", "photo", "cover"]
secret_word = random.choice(words)

clue = []
index = 0
while index < len(secret_word):
    clue.append("?")
    index = index + 1

clue = list("_____")
heart_symbol = u"\u2764"
guessed_word_correctly = False

# Main Code
unknown_letters = len(secret_word)
def update_clue(guessed_letter, secret_word, clue, unknown_letters):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
            unknown_letters = unknown_letters - 1
        index = index + 1

    return unknown_letters

difficulty = input("""Choose difficulty (Type 1, 2, or 3):\n 1 Easy\n 2 Normal\n 3 Hard\n
>>> """)

difficulty = int(difficulty)

if difficulty == 1:
    lives = 12
elif difficulty == 2:
    lives = 10
else:
    lives = 5

while lives > 0:
    print(clue)
    print('Lives left:'+heart_symbol*lives)
    guess = input("Guess a letter or the whole word: ")

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        unknown_letters = update_clue(guess, secret_word, clue, unknown_letters)
        time.sleep(0.7)
        print("")
    else:
        print("")
        print("Incorrect. You lose a life")
        lives = lives - 1
        time.sleep(0.7)
        print("")

    if unknown_letters == 0:
        guessed_word_correctly = True
        break

if guessed_word_correctly:
    time.sleep(1)
    print("")
    print("-------------------------------------------------------------------------")
    print("You won the game! The word was " + secret_word)
else:
    time.sleep(1)
    print("-------------------------------------------------------------------------")
    print("")
    print("You lost! The secret word was " + secret_word)
