#!/bin/python3
#https://www.hackerrank.com/challenges/30-2d-arrays/problem
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    hglass_sums = []

    #for _ in range(6):
    #    arr.append(list(map(int, input().rstrip().split())))
    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            #print(arr[i][j],arr[i][j+1],arr[i][j+2])
            #print(" ", arr[i+1][j+1], " ")
            #print(arr[i+2][j],arr[i+2][j+1],arr[i+2][j+2])
            hglass_sums.append(sum([arr[i][j],arr[i][j+1],arr[i][j+2],arr[i+1][j+1],arr[i+2][j],arr[i+2][j+1],arr[i+2][j+2]]))
    print(max(hglass_sums))