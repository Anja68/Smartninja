# open the file "height.txt"
# it contains the height of each person in the class
# separated by a come ","

# write a program which reads the file
# saves the different heights in a list
# and calculates the average height

with open("height.txt") as file:
    a = file.read().split(",")

height_avg=0
number_of_people=len(a)
for i in a:
    height_avg += int(i)

height_avg=height_avg/number_of_people

print(height_avg)