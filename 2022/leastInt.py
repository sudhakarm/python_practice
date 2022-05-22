def solution(A):
    # write your code in Python 3.6
    least=1
    max_num = max(A)
    if(max_num<=1):
        return least
    for i in range(1,max_num+1):
        if(i not in A):
              return i
    if(max_num > 1):
        least = max_num+1
    return least

#A = input().split(" ")
#A = [1,-1,3,5]
A = [1, 3, 6, 4, 1, 2]
A = [1,2,3]
A = [-1,-3]
print(A)
print('sol',solution(A))
