# open the file "height.txt"
# it contains the height of each person in the class
# save its content as a list
# find out what the average height is

# Hint 1: you cannot use json here
# Hint 2: Here is some code that calculates the average of a list

with open("height.txt", "r") as f:
    content_list = f.read().split(",")

avg_height = 0
for i in content_list:
    avg_height += int(i)
    avg_height = avg_height/len(content_list)
    print("The average is", avg_height)

