class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        if len(s)==2:
            if s[0]==s[1]:
                return s
            else:
                return s[0]
        
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        result = tuple()
        longpath = 0
        change = False
        
        for i in range(len(s)):
            dp[i][i] = 1
            
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                dp[i][i+1] = 1
                if not change:
                    result = (i,i+1)
                    longpath = 2
                    change = True
                    
        step = len(s)-2
        while step>0:
            j = len(s)-step
            for i in range(step):
                if s[i]==s[i+j]:
                    if dp[i+1][i+j-1] == 1:
                        dp[i][i+j] = 1
                        if j+1 > longpath:
                            result = (i,i+j)
                            longpath = j+1
            step-=1
        
        
        return s[result[0]:result[1]+1] if longpath>0 else s[0]