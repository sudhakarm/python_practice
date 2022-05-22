#{
# An array A consisting of N different integers is given. 
# The array contains integers in the range [1..(N + 1)], 
# which means that exactly one element is missing.
# #}

def solution(A):
    l = len(A)
    sumofA = sum(A)
    if l == 0 or sumofA == 0:
        return 1
    sumofnplus1 = int(((l+1)*(l+2))/2)
    return sumofnplus1-sumofA

A = [2,3,1,5]
A = [1]
#A = []
print(solution(A))
