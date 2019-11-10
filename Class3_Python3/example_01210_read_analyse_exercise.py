# open the file "height.txt"
# it contains the height of each person in the class
# save its content as a list
# find out what the average height is

with open("height.txt","r") as heights:
    content = heights.read().split("/")
