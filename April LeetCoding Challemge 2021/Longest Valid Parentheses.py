class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s)==0: return 0
        dp = [0]*(len(s)+1)
        s = " "+s
        
        for i in range(len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2]+2
                else:
                    if s[i-dp[i-1]-1]=="(":
                        dp[i] = dp[i-dp[i-1]-2]+2+dp[i-1]
                    else:
                        dp[i] = 0
                        
        return max(dp)