# Task 1

# define 2 variable and give them the values 2 and 10, then calculate the result of the division 2/10.
# print the result
var1 = 2
var2 = 10

# write your code here
result = var1 / var2
print(result)



# Task 2

# save your first name and last name as string, and concat them to 1 variable,
# and print the result

# write your code here
var3 = "Anja"
var4 = "Leherbauer"
name = var3 + " " + var4
print(name)
print(var3, var4)



# Task 3

# divide a number by 0, what happens?

# write your code here


try:
    1/2.0
    print("success")
except:
    print("tried to divide by zero, please stop")
