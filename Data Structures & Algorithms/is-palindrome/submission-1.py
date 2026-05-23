class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        st = ''.join(c for c in s.lower() if c.isalnum())

        i = 0
        j = len(st) - 1

        while i <= j:
            if st[i] == st[j]:
               i += 1
               j -= 1
            else:
               return False
        return True 