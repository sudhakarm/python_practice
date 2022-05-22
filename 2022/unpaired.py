#{#
# A non-empty array A consisting of N integers is given. 
# The array contains an odd number of elements, and each element of the array can be 
# paired with another element that has the same value, except for one element that is left unpaired.
# For example, given array A such that:

#   A[0] = 9  A[1] = 3  A[2] = 9
#   A[3] = 3  A[4] = 9  A[5] = 7
#   A[6] = 9
# the function should return 7, 
# }
def solution(A):
    # write your code in Python 3.6
    l = len(A)
    if l == 0 or (l > 0 and l%2 == 0):
        return 1
    K = {}
    for i in A:
        if i not in K:
            K[i]=1
        else:
            K[i]+=1
    for x in K:
        if K[x]%2 != 0:
            return x
    return None

A = [9,3,9,3,9,7,9]
A = [43]
print(solution(A))