import matplotlib.pyplot as plt

# We want to analyse which districts of Vienna
# have the most bicycle stands

district_list=[] # we create an empty list
with open("FAHRRADABSTELLANLAGEOGD.txt","r") as file:
    data = file.read()
    # first we split with the "newline" character
    data_list_split= data.split("\n")
    # then we iterate through the list
    for i in range(1,len(data_list_split)-1):
        # we split the elements of the list with the coma ","
        # thereby creating a new list
        x = data_list_split[i].split(",")
        # and extract the district number (elemnt index 4)
        # and append it to our district list
        district_list.append(x[4])

# district_list is a now a list with the district number
# corresponding to each bike stand
print("district_list=",district_list)

# we now count how often which district occurs in district_list
district=[0]*23
print(district)

for i in district_list:
    district[int(i)-1]+=1

# now we print the results
for i in range(len(district)):
    print("The", i+1,"district has:", district[i], "bike stations")


'''
plt.bar(list(range(1,len(district)+1)),district)
plt.xlabel("District number")
plt.ylabel("Number of bike stands")
plt.show()
'''