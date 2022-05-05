def calPoints(ops) -> int:
    """
    :type ops: List[str] - list of operations
    :rtype: int - Sum of scores after performing all operations
    """
  
    result = None
    if(len(ops) > 1000 or len(ops) < 1):
        retun result
    l=[]
    for i in range(len(ops)):
        if(ops[i].isdigit()):
            l.append(int(ops[i])
        elif(len(l)>0):
            if(ops[i]=='C'):
                l.pop()
            elif(ops[i]=='D'):
                d = l[-1]*2
                l.append(d)
            elif(ops[i]=='+' and len(l)>=2):
                d = l[-1]+l[-2]
                l.append(d)
    result = sum(l)
    return result
               
if __name__ == '__main__':
    line = input()
    ops = line.strip().split()
    print(calPoints(ops))
