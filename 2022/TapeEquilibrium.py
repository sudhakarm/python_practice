#{
# A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.
# Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: 
# A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
# The difference between the two parts is the value of: 
# |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
#  for i in range(N-1): <-- this is O(n^2) solution
#       #print(A[:i+1],A[i+1:])
#        diff = abs(sum(A[:i+1])-sum(A[i+1:])) 
#
#
# #}

def solution(A):
    P =  float('inf')
    N = len(A)
    left_sum = 0
    right_sum = sum(A)
    if N<=1:
        return 0
    for i in range(N-1):
        left_sum += A[i]
        right_sum -= A[i]
        diff = abs(right_sum-left_sum)
        if(diff==0):
            return 0
        if(diff < P):
            P = diff
    return P

A = [3,1,2,4,3]
#A = [-4,2,-3,4,-3,6,-4,2,-3,4,-3,6,4,2,3,4,-3,-6,-4,2,3,4,-3,-6,-4,2,-3,4,5,-6,2,5,8,-2,-4,5,2,9]
#A = [10, 2, 9, 3, 5, 6, 7, 3, 4, 5, 6, 4, 6, 7, 5, 4, 6, 7, 4, 6, 8, 3, 2, 4, 5, 6, 7, 8, 9, 96, 5, 43, 45, 72, 34, 5, 62, 1, 2, 34, 5, 73, 4, 6]

print(solution(A))