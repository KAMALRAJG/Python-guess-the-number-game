## Guess the number game
import random

# Generate a random secret number between 1 and 100
num = random.randint(1, 100)

guesses = []  # Initialize an empty list to store guesses

while True:
    guess = int(input("I'm thinking of a number between 1 and 100.\nWhat is your guess? "))

    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue

    guesses.append(guess)

    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break

    if len(guesses) == 1:
        if abs(num - guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
    else:
        if abs(num - guess) < abs(num - guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
