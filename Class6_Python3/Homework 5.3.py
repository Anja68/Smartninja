import random
countries_cities = {"Austria": "Vienna", "Croatia": "Zagreb", "Spain": "Madrid", "Slovenia": "Ljubljana"}

def repeat():
    while True:
        z = input("Would you like to play again?(y/n)")
        if z.lower() == "y":
            print("let's play again then!")
            return 1
        elif z.lower() == "n":
            print("alright, see you later then!")
            return 0
        else:
            print("wrong input. please enter 'y' or 'n'")

print("Welcome to the capitals game!")

while True:
    x = random.choice(list(countries_cities.keys()))
    print("what is the capital of: ", x, "?")
    y = input("enter here: ")
    if countries_cities[x].upper() == y.upper():
        print("Con Gratulations! You guessed correctly")
        z=repeat()
        if z == 1:
            continue
        elif z == 0:
            break
    else:
        print("incorrect! try again")



