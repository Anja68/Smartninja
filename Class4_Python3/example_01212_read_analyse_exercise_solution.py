# open the file "height.txt"
# it contains the height of each person in the class
# separated by a come ","

# write a program which reads the file
# saves the different heights in a list
# and calculates the average height

# Hint 1: you cannot use json here
# Hint 2: Here is some code that calculates the average of a list

list=["1","2","3","4","5","6"]
avg=0
for i in list:
    avg += int(i)
avg=avg/len(list)
print("The average of list is:",avg)

########################################
with open("height.txt") as file:
    list_of_heights = file.read().split(",")

avg=0
for i in list_of_heights:
    avg += int(i)
avg=avg/len(list_of_heights)
print("The average height is:",avg)