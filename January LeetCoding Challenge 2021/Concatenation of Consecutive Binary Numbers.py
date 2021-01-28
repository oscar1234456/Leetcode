class Solution:
    def concatenatedBinary(self, n: int) -> int:
        module = 10**9 + 7
        tempBin = ""
        for i in range(1,n+1):
            tempBin += bin(i)[2:]
        
        return int(tempBin,2) % module

#Practice: implement bin to dec, dec to bin
# count = 0
# def DecimalToBinary(num):
#     res = "0"
#     if num >= 1:
#         res = DecimalToBinary(num // 2)
#     if num != 0:
#         return res + str(num % 2)
#     return res
    
# print(DecimalToBinary(3))
# print("count",count)
# print(bin(5))

# def BinaryToDecimal(num):
#     res = 1
#     for i in num[1:]:
#         res *= 2
#         if i=="1":
#             res+=1
#     return res

# print(BinaryToDecimal("1000"))