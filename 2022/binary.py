from sys import argv


#A binary gap within a positive integer N is any maximal sequence of consecutive zeros 
# that is surrounded by ones at both ends in the binary representation of N.
#
#For example, number 9 has binary representation 1001 and contains a binary gap of length 2. 
# The number 529 has binary representation 1000010001 and contains two binary gaps

def solution(N):
    gap=0
    nbin= format(N, "b")
    print(nbin)
    m=0
    l = [0]
    for i in nbin:
        if(int(i)==1):
            #print(m)
            if(m>0):
                l.append(m)
                m=0
        else:
            m=m+1
    gap = max(l)    
    return gap

N = 1000

print(solution(N))
