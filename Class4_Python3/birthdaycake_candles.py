#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
kerzen = [3, 2, 1, 3]
print(max(kerzen))


def birthdayCakeCandles():

    candels_blowout = 0
    maximum = max(kerzen)

    for i in kerzen:
        if i == maximum:
            candels_blowout += 1

    print(candels_blowout)

birthdayCakeCandles()


