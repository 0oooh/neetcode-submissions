class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        dict_st = {}
        for i in range(len(s)):
            if s[i] not in dict_st:
                dict_st[s[i]] = 1
            else:    
                dict_st[s[i]] += 1

        for j in range(len(t)):
            if t[j] in dict_st:
                dict_st[t[j]] -= 1
            elif t[j] not in dict_st:
                return False

            if dict_st[t[j]] < 0:
                return False

        return True

