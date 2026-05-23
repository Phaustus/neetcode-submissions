class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        m = {}
        n = {}

        for i in s:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
            
        for i in t:
            if i in n:
                n[i] += 1
            else:
                n[i] = 1

        if m == n:
            return True
        else:
            return False