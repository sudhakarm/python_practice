def solution(X, A):
    # write your code in Python 3.6
  
    l = len(A)
    if(X<=0 or l==0 or X not in A):
        return -1
    if(l==1 and X==1):
        return 0
    counter = [0] * X
    steps = X
    for i in range(l):
        if(A[i] >0 and A[i] <= X and counter[A[i]-1]==0 ):
            counter[A[i]-1] = 1
            steps -= 1
        if(steps == 0):
            return i
    return -1

A = [1,3,2,4,2,4,5,3,5,4,6]
X = 5
A=[1]
X=1
print(solution(X,A))