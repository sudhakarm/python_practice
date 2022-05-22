def counting(A,m):
    n = len(A)
    count = [0] * (m+1)
    print(count)
    for k in range(n):
        count[A[k]] += 1
    return count

A = [2,0,1,0,2,1,3,6]
print(counting(A,6))
# m should be max(A)