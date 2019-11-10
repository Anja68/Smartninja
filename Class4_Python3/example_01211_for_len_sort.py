# useful list functions

# to sort a list we can use the sort function
data = [1,22,34,56,23,65,34,98,73,27]
data.sort() # to sort in a ascending fashion
print(data)

# to sort in descending order
data.sort(reverse=True)
print(data)

print(10*"*")

# to find the length of a list
# we can use the len() function
x = len(data)
print(x) # 10 -> there are 10 elements in the list

# can be useful whilst listing elements in a for loop

for i in range(len(data)):
    print("the element number",i,"is",data[i])

print(sum(data))