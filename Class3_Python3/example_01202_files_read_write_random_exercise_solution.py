# write a list with the ingredients salad, orange, mango
# choose randomly an ingredient, and write it to a file called "random_fruit.txt"
import random
fruit_list = ["salad", "orange", "mango"]
random_fruit = random.choice(fruit_list)

with open("random_fruit.txt", "w") as f:
    f.write(random_fruit)
