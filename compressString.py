# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
c = 1
n = len(s)
def print_res(x,c):
    print("(",x,", ",c,") ",sep='',end='')
for i in range(n):
    if(i == n-1):
        print_res(c,s[i]);
    else:
        if(s[i] == s[i+1]):
            c += 1
        else:
            print_res(c,s[i]);
            c = 1