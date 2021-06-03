class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1Length = len(s1)
        s2Length = len(s2)
        s3Length = len(s3)
        if s1Length+s2Length != s3Length:
            return False
        if s1Length==0 and s2Length==0:
            return True
        
        dp = [[False for __ in range(s2Length+1) ] for _ in range(s1Length+1)]
        # print(dp)
        dp[0][0] = True
        
        for i in range(s1Length+1):
            for j in range(s2Length+1):
                #i=0 first row
                if i==0:
                    if j>0:
                        dp[0][j] = (s2[j-1]==s3[j-1]) and dp[0][j-1]
                    continue
                #j=0 first row
                elif j==0:
                    dp[i][0] = (s1[i-1]==s3[i-1]) and dp[i-1][0]
                    continue
                else:
                    if s3[i+j-1]==s1[i-1]:
                        dp[i][j] = dp[i-1][j]
                    if s3[i+j-1]==s2[j-1]:  
                        dp[i][j] = (dp[i][j] or dp[i][j-1])
        # print(dp)
        return dp[s1Length][s2Length]