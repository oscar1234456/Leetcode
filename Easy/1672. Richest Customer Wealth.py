class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxTotal = 0
        for customers in accounts:
            temp = 0
            for money in customers:
                temp += money
            maxTotal = temp if (temp>maxTotal) else maxTotal
        return maxTotal
                
# Runtime: 44 ms, faster than 98.58% of Python3 online submissions for Richest Customer Wealth.
# Memory Usage: 14.1 MB, less than 84.90% of Python3 online submissions for Richest Customer Wealth.