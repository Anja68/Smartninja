# ask for a number to be inputted, and save it in a variable
# if the number is bigger than 1000, print You entered a very big number
# otherwise print The number is cute

eingabe = input ("Bitt eine Nummer eingeben:")

mynumber = float(eingabe)

print(f"Deine Eingabe ist {mynumber}")

if mynumber > 1000:
    print("You entered a high number")
else:
    print("The number is cute")

