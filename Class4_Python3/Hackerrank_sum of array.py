#!/bin/python3

import os
import sys
import json

#
# Complete the simpleArraySum function below.
#
ar = [1, 2, 3, 4, 10, 11]
print(sum(ar))

with open("meineliste.txt", "w") as f:
    f.write(json.dumps(ar))

def simpleArraySum():
    #
    # Write your code here.
    #
    with open("meineliste.txt", "r") as f:
        content_list = json.loads(f.read())
        print(content_list)

    x = 0
    for i in content_list:
        x += int(i)
    print(x)

simpleArraySum()

# n = input()
# l = list(map(int, input().split(' ')))
# print(sum(l))