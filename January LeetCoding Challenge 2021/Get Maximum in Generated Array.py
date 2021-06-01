class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        result = list()
        
        for i in range(n+1):
            if i == 0:
                result.append(0)
                continue
            elif i == 1:
                result.append(1)
                continue
            mod = i%2
            if mod==0:
                result.append(result[i//2])
            else:
                s = (i-1)//2
                result.append(result[s]+result[s+1])
        return max(result)
# O(n)