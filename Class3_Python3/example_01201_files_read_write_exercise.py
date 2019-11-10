# write a list with the ingredients salad, orange, mango
# choose one element of the list
# and write it to a file called "fruit.txt"


meineliste = ["salad", "orange", "mango"]

with open("fruit.txt", "w") as f:
    f.write(meineliste[1])