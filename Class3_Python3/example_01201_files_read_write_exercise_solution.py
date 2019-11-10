# write a list with the ingredients salad, orange, mango
# choose one element of the list
# and write it to a file called "fruit.txt"
fruit_list = ["salad", "orange", "mango"]


with open("fruits.txt", "w") as f:
    f.write(fruit_list[1])