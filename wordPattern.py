class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if(len(s)!=len(pattern)):
            return False
        dic_p ,dic_s = {},{}
        for i in range(len(pattern)):
            if(pattern[i] in dic_p and dic_p[pattern[i]]!=s[i]):
                return False
            if(s[i] in dic_s and dic_s[s[i]]!=pattern[i]):
                return False
            dic_p[pattern[i]] = s[i]
            dic_s[s[i]] = pattern[i]
        return True