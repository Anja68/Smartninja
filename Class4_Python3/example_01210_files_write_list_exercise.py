# save the following list in a file
# using one of the methods discussed previously
import json

continents = ["Asia","Africa","North America","South America","Antarctica","Europe","Oceania"]

filename = "kontinente.txt"

with open (filename,"w") as f:
    f.write(json.dumps(continents))


