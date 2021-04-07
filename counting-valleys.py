#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    base=hike=0
    for step in range(steps):
        if(path[step]=='U'): 
            base += 1
            if(base == 0): hike +=1 #catch here is, only increase hike if its equal to sea level and it is up
        elif(path[step]=='D'): base -= 1
    return hike

if __name__ == '__main__':
    fptr = open("countingvalley.out", 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()