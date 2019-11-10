# Write a loop, which asks for an input,
# until you entered a valid operator

# hint:
# "+" in "+-/*"
# "+" in ["*", "+", "-", "/"]
print("+-" in "+-/*")                # True
print("+-" in ["*", "+", "-", "/"])  # False

eingabe = None
while eingabe not in ["*", "+", "-", "/"]:
    eingabe = input("Bitte einen gültigen Operator eingeben: ")
else:
    print("Gültiger Operator")