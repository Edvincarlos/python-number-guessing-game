import random

secret = random.randint(1, 100)
print("Guess the number between 1 and 100")

while True:
    try:
        guess = int(input("Your guess: "))
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("You got it!")
            break
    except ValueError:
        print("Please enter a number!")
