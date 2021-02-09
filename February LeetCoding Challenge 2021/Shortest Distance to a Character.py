class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:            
            l = [i for i in range(len(s)) if s[i] == c]
            ans = []
            for i in range(len(s)):
                ans.append(min([abs(i - j) for j in l]))
            return ans