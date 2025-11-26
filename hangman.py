import random

words = ["apple", "banana", "orange", "grapes", "mango"]
word = random.choice(words)
guessed = []
tries = 6

print("Welcome to Hangman Game!")
print("_ " * len(word))

while tries > 0:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one valid letter.")
        continue

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.append(guess)

    if guess not in word:
        tries -= 1
        print("Wrong guess! Tries left:", tries)

    display = ""
    for letter in word:
        display += (letter + " ") if letter in guessed else "_ "
    print(display.strip())

    if all(letter in guessed for letter in word):
        print("You guessed the word:", word)
        break

if tries == 0:
    print("Game over! The word was:", word)
