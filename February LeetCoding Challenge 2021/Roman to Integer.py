class Solution:
    def romanToInt(self, s: str) -> int:
        romanToInt = {"I":1,"V":5,"X":10, "L":50, "C":100, "D":500, "M":1000}
       
        i = len(s)-1
        res = 0
        while i>=0:
            now = s[i]
            nextOne = s[i-1] if i-1 >=0 else None
            if nextOne:
                #have next Roman
                if romanToInt[now] <= romanToInt[nextOne]:
                    #Ex. VI, II
                    res+=romanToInt[now]
                else:
                    #Ex. IV
                    res+=(romanToInt[now]-romanToInt[nextOne])
                    i-=1
            else:
                res += romanToInt[now]
            i-=1
        
        return res