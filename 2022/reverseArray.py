from re import I


def reverse(A):
    N = len(A)
    for i in range(N//2):
        k = N-i-1
        print(i,k)
        A[i], A[k] = A[k], A[i]
    return A
A = [3,2,4,8,5,6,1,2]
print(reverse(A))