import random


def get_positive_int(prompt):
    while True:
        try:
            n = int(input(prompt))
        except ValueError:
            pass
        else:
            if n > 0:
                return n


def main():
    level = get_positive_int("Level: ")
    secret = random.randint(1, level)

    while True:
        guess = get_positive_int("Guess: ")
        if guess < secret:
            print("Too small!")
        elif guess > secret:
            print("Too large!")
        else:
            print("Just right!")
            break


main()
