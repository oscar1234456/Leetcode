class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1 if dividend ^ divisor >=0 else -1
        res = 0
        
        dividend, divisor = abs(dividend),abs(divisor)
        
        for power in range(31,-1,-1):
            if (divisor<<power)<=dividend:
                res += (1<<power)
                dividend -= (divisor<<power)
            
        res = res*sign
        
        if not (-2**31<=res<=2**31-1):
            return 2**31-1
        else:
            return res