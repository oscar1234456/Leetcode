class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[-1]*(len(s)) for i in range(len(s))]
        L = 0
        R = len(s)-1
        sequence = s
        return self.solve(dp, sequence, L, R)
        
        
    def solve(self, dp, sequence, L, R):
        if L > R: return 0
        elif L==R: return 1
        elif dp[L][R] != -1:
            return dp[L][R]
        elif sequence[L] == sequence[R]:
            dp[L][R] = 2 + self.solve(dp, sequence, L+1, R-1)
        else:
            moveL = self.solve(dp, sequence, L+1, R)
            moveR = self.solve(dp, sequence, L, R-1)
            dp[L][R] = max(moveL, moveR)
        return dp[L][R]


# Runtime: 848 ms, faster than 89.61% of Python3 online submissions for Longest Palindromic Subsequence.
# Memory Usage: 23.4 MB, less than 85.64% of Python3 online submissions for Longest Palindromic Subsequence.
