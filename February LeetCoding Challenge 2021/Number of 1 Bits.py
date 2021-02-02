# solution 1: 52ms
class Solution:
    def hammingWeight(self, n: int) -> int:
        return self.DecimalToBinary(n)
        
        
    def DecimalToBinary(self,num):
        count = 0
        if num >= 1:
            count = self.DecimalToBinary(num // 2)
        if num != 0:
            return (count + 1) if num % 2 else count
        return count
        

# solution2 :12ms (other people)
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         res = 0
#         while n>0:
#             res += n&1
#             n = n>>1
#         return res