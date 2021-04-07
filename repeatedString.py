#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    if(n > 10**2): return 0
    mod = n%len(s)
    last = s[0:mod].count('a') if(mod > 0) else 0
    repeatX = n//len(s)
    perstring = s.count('a')
    ans = (perstring*repeatX)+last
    print(ans,last,repeatX,perstring)   
    return ans

if __name__ == '__main__':
    fptr = open("4.out", 'w')
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    print(str(result))
    fptr.write(str(result) + '\n')
    fptr.close()
