# Modify the secret number game code below such
# that it shows the number of attempts
# after each failed attempt

# Modify the secret number game code below such
# that it shows the number of attempts
# after each failed attempt

secret = "7"
versuche = 0

while versuche < 5:
    guess = input("Guess the secret number: ")
    versuche += 1

    if guess == secret:
        print("Oh, so great!, you won!")
        break
    else:
        print(f"Oh no, please try again. This was your {versuche}. try")

else:
    print("Das wars!")