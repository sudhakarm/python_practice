from itertools import permutations
import re

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        #first make different combinations of given words
        perm_list = list(map("".join,permutations(words)))
        outList = []
        
        for word in perm_list:
            for m in re.finditer(word, s):
                #print(word+' found', m.start(), m.end())
                outList.append(m.start())
        return set(outList) #returns unique list

s = "barfoothefoobarman"
words =  ["foo","bar"]
sol = Solution()
print(sol.findSubstring(s,words)) #should print [0,9] or [9,0]
