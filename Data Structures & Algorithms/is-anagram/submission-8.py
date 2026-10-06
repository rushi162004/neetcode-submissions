class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_3 = {}
        s_4 = {}
        for value in set(s):
            s_3[value] = s.count(value)
        for value in set(t):
            s_4[value] = t.count(value)
        if s_3 == s_4:
            return True
        else:
            return False