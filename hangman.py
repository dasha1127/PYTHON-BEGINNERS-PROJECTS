import random

words = ['dasha', 'disha', 'sagar', 'pizza']
word = random.choice(words)
guessed = "_" * len(word)
guessed_correctly = set()
attempts = 6

while attempts > 0 and "_" in guessed:
    print(guessed)
    guess = input("Guess a letter: ").lower()

    if guess in guessed_correctly:
        print("You already guessed that letter.")
        continue

    if guess in word:
        guessed_correctly.add(guess)
        guessed = "".join([letter if letter in guessed_correctly else "_" for letter in word])
    else:
        attempts -= 1
        print(f"Wrong guess. You have {attempts} attempts left.")

if "_" not in guessed:
    print(f"Congratulations! You guessed the word: {word}")
else:
    print(f"Sorry, you ran out of attempts. The word was: {word}")
import random

words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
guessed = "_" * len(word)
guessed_correctly = set()
attempts = 6

while attempts > 0 and "_" in guessed:
    print(guessed)
    guess = input("Guess a letter: ").lower()

    if guess in guessed_correctly:
        print("You already guessed that letter.")
        continue

    if guess in word:
        guessed_correctly.add(guess)
        guessed = "".join([letter if letter in guessed_correctly else "_" for letter in word])
    else:
        attempts -= 1
        print(f"Wrong guess. You have {attempts} attempts left.")

if "_" not in guessed:
    print(f"Congratulations! You guessed the word: {word}")
else:
    print(f"Sorry, you ran out of attempts. The word was: {word}")
