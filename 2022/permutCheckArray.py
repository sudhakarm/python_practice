#{
#check if the array A is having all permutations or not.
# if A = [1,2,3,4] is 1 and A = [2,3,4] is 0
#}
def solution(A):
    L = len(A)
    if L != max(A):
        return 0
    permSum = (L*(L+1))//2
    if permSum == sum(set(A)):
        return 1
    return 0

A = [9, 5, 6, 3, 2, 7, 4, 1, 10, 8] 
print(solution(A))
