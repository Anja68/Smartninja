
# iterate through this dict, and print its keys and values
capitals = {"France": "Paris",
            "Iceland": "Reykjavik",
            "Denmark": "Copenhagen",
            "Litauen": "Vilnius",
            "Canada": "Ottawa",
            "Austria": "Wien"}

for i in capitals: # iterates over keys
    print(i, capitals[i])

print()

for country in capitals.keys():
    print(country)

print()

    # we can unpack in forloop
for capital in capitals.values():
    print(capital)