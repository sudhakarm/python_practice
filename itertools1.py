#itertools1.py
from itertools import *

count=com_count=0
n = int(input())
n_string = input().split()
k_index = int(input())

for c in combinations(n_string, k_index):
    count+=1
    if k_value in c:
        com_count+=1
print(round(com_count/count,12))

###Alternate sol ######
#C = list(combinations(L, K))
#F = filter(lambda c: 'a' in c, C)
#print("{0:.3}".format(len(list(F))/len(C)))

