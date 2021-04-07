#!/bin/python3

import math
import os
import random
import re
import sys


dict = {}
if __name__ == '__main__':
    s = input()
    for i in s:
        if i in dict: dict[i] += 1
        else: dict[i] = 1
    
    dict2 = sorted(sorted(dict), key = dict.get, reverse = True)
    #print(dict2)
    for j in dict2[:3]:
        print(j, dict[j])