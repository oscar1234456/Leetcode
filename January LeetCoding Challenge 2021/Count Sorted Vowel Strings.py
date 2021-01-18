class Solution:
    def countVowelStrings(self, n: int) -> int:
        return self.count("a",n-1)+self.count("e",n-1)+self.count("i",n-1)+self.count("o",n-1)+self.count("u",n-1)
    
    def count(self, lastChar, n):
        if n==0:
            return 1
        if lastChar=="a":
            return self.count("a",n-1)+self.count("e",n-1)+self.count("i",n-1)+self.count("o",n-1)+self.count("u",n-1)
        elif lastChar=="e":
            return self.count("e",n-1)+self.count("i",n-1)+self.count("o",n-1)+self.count("u",n-1)
        elif lastChar=="i":
            return self.count("i",n-1)+self.count("o",n-1)+self.count("u",n-1)
        elif lastChar=="o":
            return self.count("o",n-1)+self.count("u",n-1)
        else:
            return self.count("u",n-1)


#Solution2 : DP
#class Solution:
    # def countVowelStrings(self, n: int) -> int:
    #     dp = [[1 for s in range(n)] for i in range(6)]
    #     sum = 0
    #     for index in range(len(dp)-1):
    #         sum += dp[index][0]
    #     dp[5][0] = sum
        
    #     for i in range(n-1):
    #         dp[0][i+1] = dp[5][i]
    #         tempSum = dp[5][i]
    #         for j in range(1,5):
    #             dp[j][i+1] = dp[j-1][i+1]-dp[j-1][i]
    #             tempSum += dp[j][i+1]
    #         dp[5][i+1] = tempSum
    #     return dp[5][n-1]