class Solution:
    def removePalindromeSub(self, s: str) -> int:
        length = len(s)
        
        if length == 0:
            return 0
        elif s == s[::-1]:
            return 1
        else:
            return 2