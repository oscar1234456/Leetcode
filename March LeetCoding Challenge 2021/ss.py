class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        while num>0:
            if num>=1000:
                temp = num // 1000
                for _ in range(temp):
                    res += "M"
                num %= 1000
            elif num >=500:
                if num >=900:
                    res += "CM"
                    num %= 900
                else:
                    res += "D"
                    num %= 500
            elif num>=100:
                if num >= 400:
                    res += "CD"
                    num %= 400
                else:
                    temp = num // 100
                    for _ in range(temp):
                        res += "C"
                    num %= 100
            elif num >= 50:
                if num >= 90 :
                    res += "XC"
                    num %= 90
                else:
                    res += "L"
                    num %= 50
            elif num >= 10:
                if num >= 40:
                    res += "XL"
                    num %= 40
                else:
                    temp = num // 10
                    for _ in range(temp):
                        res += "X"
                    num %= 10
            elif num >=5:
                if num >= 9:
                    res += "IX"
                    num %= 9
                else:
                    res += "V"
                    num %= 5
            else:
                if num>=4:
                    res += "IV"
                    num%=4
                else:
                    temp = num // 1
                    for _ in range(temp):
                        res += "I"
                    num %= 1
                    
        return res
            
            
s = Solution()
print(s.intToRoman(4900))      
            
            
            