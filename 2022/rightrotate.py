#{
# An array A consisting of N integers is given. 
# Rotation of the array means that each element is shifted right by one index, 
# and the last element of the array is moved to the first place. 
# For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]
# #}
def solution(A, K):
    # write your code in Python 3.6
    l = len(A)
    if(l<1):
        return A
    if(K > l):
        if(K % l !=0 ):
            K = K % l
        else:
            return A
    B = A[-K:]+ A[:-K]
    return B

A = [1, 1, 2, 3, 5]
K = 3
print(solution(A,K))

#{
# 1, -2, -3, -4, -5, -.. expected [-3, -4, -5, -6, -1, -.
#got [710, 807, 568, 560, .. expected [155, 710, 807, 568
# or example, for the input ([1, 1, 2, 3, 5], 42) 
# the solution returned a wrong answer 
# (got [1, 1, 2, 3, 5] expected [3, 5, 1, 1, 2]). 
#
# #}