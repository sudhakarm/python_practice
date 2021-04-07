import math
import sys
def checkprime(n):
    if (n == 1): return False
    if (n == 2): return True
    for j in range(3,int(math.sqrt(n))+1,2):
        print(j,n)
        if n%j == 0:
            return False
    return True
    
n = int(input())
print(checkprime(n))
sys.exit()
for i in range(n):
    print('Not prime' if not checkprime(int(input())) else 'Prime')
