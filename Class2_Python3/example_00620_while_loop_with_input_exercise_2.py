# Schreibe eine while Schleife
# sie bricht nur dann ab, wenn der User "yes" oder "no" eingegeben hat
eingabe = None

while eingabe not in ["yes","no"]:
    eingabe = input("Bitte yes oder no eingeben: ")

else:
    print("Richtig!")