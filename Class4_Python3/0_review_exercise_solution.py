# read the data in the file hello.txt
# and print it in the terminal

filename = "hello.txt"
with open(filename,"r") as f:
    x = f.read()
print(x)