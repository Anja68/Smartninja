
# create a for loop, which iterates through all meals
# print the meal and the price each iteration
shoppinglist = {"bread": 100, "butter": 90, "avocado": 10}



for meal, price in shoppinglist.items():
        print(meal, price)


# Extra: sum up all prices and print the total shopping cost

price_sum = sum(shoppinglist.values())
print(price_sum)