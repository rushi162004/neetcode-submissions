class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_1 = set(s)
        s_2 = set(t)
        s_3 = {}
        s_4 = {}
        for value in s_1:
            s_3[value] = s.count(value)
        for value in s_2:
            s_4[value] = t.count(value)
        if s_3 == s_4:
            return True
        else:
            return False