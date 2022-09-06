class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ind = 0
        for i in range(len(t)):
            if(ind<len(s) and s[ind]==t[i]):
                ind+=1
        return ind==len(s)