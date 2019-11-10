# read the data in the file hello.txt
# and print it in the terminal

with open ("hello.txt", "r") as f:
    hello = f.read()

print(hello)