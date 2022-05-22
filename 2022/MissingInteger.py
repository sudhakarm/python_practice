#{
# given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
# 
# }

def solution(A):
    A = sorted(set(A))
    L = len(A)
    if L==0: 
        return 1
    M = max(A)
    sumofA = sum(A)
    if M <= 0 :
        return 1
    j=0
    for i in set(A):
        if i <= 0:
            continue
        j+=1
        if(i!=j):
            return j
    return j+1


A = [1, 3, 6, 4, 1, 2]
#A = []
#
#A = [-1,-3]
#A = [1, 4, 5, 6, 2, 8]

A = [1, 4, 5, 6, 2, 8]
A = [-1,-3]
A = [1, 2, 3]
A = [1,2,3,4,5,500000499985,6]
A = [1, 3, 6, 4, 1, 2]
A =  [1, 3, 6, 4, 1, 2]
A = [-2,1,2,-3,3,4,5,50000]
A = [0,1,2,3,4,6,7,8]
A = [-1,-2,-3,-4,-5,-6,0,1,2,3,4,5,6]
A = [-1,-2,-3,-4,-5]
print(solution(A))
