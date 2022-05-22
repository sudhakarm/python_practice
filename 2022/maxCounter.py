#{
# Max counters
# A = [1,...,K]
# N = Number of counter Ex: 3 , have to return [count of 1s, count of 2s, count of 3s]
# return counter of number of each number
# Ex : A = [1,1,2,3,4,3,1,5,4,6] return [3,1,2,1,1,1]
# if A = [1,1,1,1] return C = [4]
# if A = [2,2,2,2] return C = [0,4]
# #
# If A[K] = N+1 then operation should be max of C at that point
# https://app.codility.com/demo/results/training6ANA4U-7KE/   
# O(N + M)
# #}
def maxCounter(N,A):
    C = [0] * N
    L = len(A)
    MaxC = set()
    for i in range(L):
        if( 0 < A[i] <= N):
            C[A[i]-1] += 1
            MaxC.add(C[A[i]-1])
        elif A[i] == N+1 and len(MaxC) > 0:
            C = [max(MaxC)] * N
            MaxC.clear()
    return C

def solution2(N, A):
    
    counters = [0] * N
    max_numbers = set()
    print("Sol2: ",counters)
    for i in range(0, len(A)):
        print('max-num-->',max_numbers)
        if 1 <= A[i] <= N:

            index = A[i]-1
            counters[index] += 1
            max_numbers.add(counters[index])
            print(counters)
        elif A[i] == N + 1 and len(max_numbers) > 0:

            counters = [max(max_numbers)] * N
            max_numbers.clear()

    return counters

A = [3,4,4,6,1,4,4]
N = 5
print(maxCounter(N,A))
print(solution2(N,A))