#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i=jumps=0
    while i < len(c)-1:
        jumps+=1
        if(i+2 < len(c) and c[i+2] == 0): i+=1
        print(i,c[i],jumps)
        i+=1
    print(jumps)

if __name__ == '__main__':
    fptr = open("3.out", 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()