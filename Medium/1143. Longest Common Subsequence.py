class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1_len, text2_len = len(text1), len(text2)
        dp = [[0]*text2_len for _ in range(text1_len)]
        
        for i in range(text1_len):
            for j in range(text2_len):
                if text1[i] == text2[j]: #Last word different
                    dp[i][j] = 1 if(i==0 or j==0) else dp[i-1][j-1]+1
                else:
                    if i==0 and j==0:
                        dp[i][j] = 0 #Actually, Needn't to do this.
                    elif i>0 and j==0:
                        dp[i][j] = dp[i-1][j]
                    elif i>0 and j>0:
                        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                    elif i==0 and j>0:
                        dp[i][j] = dp[i][j-1]
        return dp[text1_len - 1][text2_len-1]

# Runtime: 452 ms, faster than 43.85% of Python3 online submissions for Longest Common Subsequence.
# Memory Usage: 21.9 MB, less than 69.91% of Python3 online submissions for Longest Common Subsequence.