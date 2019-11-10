# save the following list in a file
continents = ["Asia","Africa","North America","South America","Antarctica","Europe","Oceania"]
# using one of the methods discussed previously

# option 1 : JSON
import json

with open("continents_json.txt","w") as f:
    f.write(json.dumps(continents))

# option 2: CSV

with open("continents.csv","w") as f:
    f.write(",".join(continents))