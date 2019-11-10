# take your shopping list, "bread", "butter", "chocolate"
# you are on a diet, and decide to remove "chocolate"
# print the list before and after removing
shopping_list = ["bread", "butter", "chocolate"]
shopping_list.remove("chocolate")
#shopping_list.pop()
print(shopping_list)

# instead, you will add "proteins"
# append it to your list, and print your list
shopping_list.append("proteins")
print(shopping_list)

# extra: try adding elements to the list by
# 1) adding (+)
# 2) extending
print(shopping_list + ["soup"])
shopping_list.extend(["yoghurt", "cheese"])
print(shopping_list)