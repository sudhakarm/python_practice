#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
   pairs = 0
   for i in set(ar):
   #This set() function find out sets of similar objects in to element as key and count as value pairs
        pairs += ar.count(i)//2 
   return pairs

if __name__ == '__main__':
    fptr = open("sockMerchant.out", 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()