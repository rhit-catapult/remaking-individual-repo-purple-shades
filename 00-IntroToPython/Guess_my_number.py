import random
import os


def play_with_guesses(guesses, secret=None):
    if secret is None:
        secret = random.randint(1, 100)
    attempts = 0
    for g in guesses:
        attempts += 1
        guess = int(g)
        if guess == secret:
            return True, attempts
    return False, attempts


def main():
    print("Welcome to Guess my number 1-100")
    guess_counter = 0
    if "SECRET_NUMBER" in os.environ:
        secret_number = int(os.environ["SECRET_NUMBER"])
    else:
        secret_number = random.randint(1, 100)

    while True:
        guess_text = input("Make a Guess: ")
        guess = int(guess_text)
        guess_counter += 1
        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        else:
            print(f"Correct! You guessed it in {guess_counter} tries.")
            break


if __name__ == '__main__':
    main()