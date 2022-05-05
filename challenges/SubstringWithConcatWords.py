"""
This solution collected from https://hecodesit.com/substring-with-concatenation-of-all-words-leetcode/
look at history for my original solution, which is out of memory for long sets
"""
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        dict = collections.defaultdict(int)
        for w in words:
            dict[w] += 1
        l, res = len(words[0]), []
        for i in range(l):
            dict1 = dict.copy()
            j = i
            while j < len(s) - l + 1:
                dict1[s[j : j + l]] -= 1
                while dict1[s[j : j + l]] < 0:
                    dict1[s[i : i + l]] += 1
                    i += l
                j += l
                if (j - i) / l == len(words):
                    res.append(i)
        return res
    
s = "barfoothefoobarman"
words =  ["foo","bar"]
sol = Solution()
print(sol.findSubstring(s,words)) #should print [0,9] or [9,0]
