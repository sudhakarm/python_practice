class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        #first make different combinations of given words
        perm_list = self.findPermutations(words)
        outList = []
        for word in perm_list:
            matchIndex = s.find(word)
            if(matchIndex != -1):
                outList.append(matchIndex)
        return outList
        
    def findPermutations(self,words):
        from itertools import permutations
        return list(map("".join,permutations(words)))

s = "barfoothefoobarman"
words =  ["foo","bar"]
sol = Solution()
print(sol.findSubstring(s,words)) #should print [0,9] or [9,0]
