def isValid(s: str) -> bool:
    """
    :type s: str - String to be tested for validity
    :rtype: bool - Returns true if the string is valid else false
    """
    
    result = None
    if(len(s)<1 or len(s)>104):
        return result
    t = []
    sets = {']':'[', '}':'{', ')':'('}
    result = False
    for i in s:
        if(i not in [']', '[', '}', '{', ')', '(']):
            return result
        if(i in ['[', '(', '{']): # Opening perenthesis, add to temp list
            t.append(i)
        elif(i in [']', ')', '}']): #closing parentheses, remove only last from temp list if it matches
            if(len(t)==0): #if there is no opening parenteses character in temp list at all, return false
                retrun result
            last = t.pop() #take the last character as it matches with opening
            if(last != sets[i]):
                return result
    if len(t)==0: #after all the iterations, the pairs get removed. Hence the valid string should empty the temp list.
        result = True
    return result

if __name__ == "__main__":
    line = input()
    if isValid(line):
        print("valid")
    else:
        print("invalid")
             
