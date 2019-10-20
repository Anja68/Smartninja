# print welcome to user
print("Willkkommen beim Calculator")


# read user input for operation
operator = input("Bitte einen Operator (+,-,*,/) eingeben ")

# read user input for first value
eingabe1 = float(input("Bitte Zahl 1 eingeben: "))
print(f"You entered {eingabe1}")


# read user input for second value
eingabe2 = float(input("Bitte Zahl 2 eingeben: "))
print(f"You entered {eingabe2}")

# calculate depending on operators
# and print result
if operator == "+":
    print(eingabe1 + eingabe2)
elif operator == "-":
    print(eingabe1 - eingabe2)
elif operator == "/":
    print (eingabe1 / eingabe2)
elif operator == "*":
    print (eingabe1*eingabe2)
else:
    print ("Falsche Eingabe")



