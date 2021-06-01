#Solution 1: better brute force
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        
        arrayLength = len(A)
        count = 0
        
        
        for i in range(arrayLength):
            now = i
            flag = False
            diff = 0
            tempCount = 0
            for j in range(2):
                if now+1 < arrayLength:
                    if flag:
                        if A[now+1]-A[now] == diff:
                            tempCount += 1
                    else:
                        diff = A[now+1]-A[now]
                        tempCount+=1
                        flag = True
                else:
                    break
                now += 1
            if tempCount == 2:
                count+=1
                while now+1<arrayLength:
                    if A[now+1]-A[now] == diff:
                        count += 1
                    else:
                        break
                    now += 1
                    
        return count
                        

#solution2 : DP
# class Solution:
#     def numberOfArithmeticSlices(self, A: List[int]) -> int:
#         dp = [0 for _ in range(len(A))]
#         res = 0
#         for i in range(2,len(A)):
#             if A[i-2] - A[i-1] == A[i-1] - A[i]:
#                 dp[i] = dp[i-1]+1
#                 res += dp[i]
                
#         return res
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        