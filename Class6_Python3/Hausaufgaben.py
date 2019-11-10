# Guessing Game (While-Schleife)

secret = 42
guess = 0
counter = 0
limit = 10

while counter<limit:
    guess = int(input("Enter a number with two figures: "))
    counter += 1

    if guess == secret:
        print("Your guess is correct!")
        print("You have tried", counter, "times")

    elif guess < secret:
        print("Wrong! Your guess is too small")
        print("You have tried", counter, "times")

    else:
        print("Wrong! Your guess is too big")
        print("You have tried", counter, "times")