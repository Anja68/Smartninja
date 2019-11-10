import json
# Dictionaries

outfit = {"Size":"L", "Colour":"Blue", "Type":"T-shirt"}

print(outfit["Type"])   # selecting elements

outfit["Size"]="S"  # changing elements
print(outfit)

outfit["Brand"]="H&M" # adding new elements
print(outfit)

# storing in file
with open("Clothing.txt","w") as f:
    f.write(json.dumps(outfit))

