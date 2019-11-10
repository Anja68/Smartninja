import json

# writing into file & reading from files

f=open("My_File.txt","w")
text= "Some random text"
f.write(text)

f.close()
f=open("My_File.txt","r")
text_2=f.read()
print(text_2)
f.close()
# Writing lists into files

some_list = ["1","2","3"]

filename = "numbers.csv"

# CSV = Comma Separated Values
with open(filename,"w") as f:
    content = ",".join(some_list) # join elements by adding a "," in-between, creates a string
    f.write(content)

with open(filename,"r") as f:
    content = f.read()
    a_list= content.split(",")  # separate by "," and create list
    print(a_list)

print("FINISHED WRITING AND READING CSV-FILE")
# JSON

filename = "numbers.txt"

with open(filename, "w") as f:
    f.write(json.dumps(some_list))

with open(filename, "r") as f:
    content = json.loads(f.read())
    print(content)

print("FINISHED WRITING AND READING TXT-FILE")
