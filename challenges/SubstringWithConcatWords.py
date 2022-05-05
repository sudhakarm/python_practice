from itertools import permutations

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        #first make different combinations of given words
        perm_list = list(map("".join,permutations(words)))
        outList = []
        
        for word in perm_list:
            index=0
            while index < len(s):
                index = s.find(word, index)
                if index == -1:
                    break
                outList.append(index)
                index += 1    
        return set(outList) #returns unique list

s = "barfoothefoobarman"
words =  ["foo","bar"]
sol = Solution()
print(sol.findSubstring(s,words)) #should print [0,9] or [9,0]
