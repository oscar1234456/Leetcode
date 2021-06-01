class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        maxEvenComplete = False
        while not maxEvenComplete:
            maxEvenComplete = True
            nums.sort()
            maxEven = 0
            maxOdd = 0
            #find maxEven
            for i in range(len(nums)-1,-1,-1):
                if nums[i]%2==0:
                    maxEven = nums[i]
                    break

            #find maxOdd
            for i in range(len(nums)-1,-1,-1):
                if nums[i]%2!=0:
                    maxOdd = nums[i]
                    break
            if maxEven!=0:
                nums.remove(maxEven)
            else:
                break
            while(maxEven>maxOdd and maxEven%2==0):
                maxEvenComplete = False
                maxEven//=2
            nums.append(maxEven)
            
        # print(nums)
        minOddComplete = False
        while not minOddComplete:
            minOddComplete = True
            flag = False
            nums.sort()
            minOdd = 0
            maxEven = 0
            maxOdd = 0
            #find maxEven
            for i in range(len(nums)-1,-1,-1):
                if nums[i]%2==0:
                    maxEven = nums[i]
                    break
            if maxEven==0:
                flag = True
                #find maxOdd
                for i in range(len(nums)-1,-1,-1):
                    if nums[i]%2!=0:
                        maxOdd = nums[i]
                        break
            # print(maxEven)

            #find minOdd
            for item in nums:
                if item%2!=0:
                    minOdd = item
                    break
            if minOdd!=0:
                nums.remove(minOdd)
            else:
                break
            if not flag:
                while(minOdd*2<=maxEven and minOdd%2!=0):
                    minOddComplete = False
                    minOdd*=2
            else:
                # print("in")
                # print("maxOdd",maxOdd)
                # print("minOdd",minOdd)
                now = maxOdd - minOdd
                apr = abs(minOdd*2 - maxOdd)
                if apr<now:
                    minOdd *= 2
                
            nums.append(minOdd)
       
        if not flag:
            minNums = min(nums)
            maxNums = max(nums)
            nums.remove(minNums)
            while(minNums%2!=0 and minNums<=maxNums):
                minNums *=2
                if minNums>=maxNums:
                    break
            nums.append(minNums)
            # print(maxNums)
            # print(minNums)
        print(nums)
        return max(nums)-min(nums)
        
        
        
# Failed, textcase: 49/76
# 偶數最大下降到最低（剪之前不會低於奇數最高）
# 奇數最小升到最高（不能升到偶數最高）


# class Solution:
#     def minimumDeviation(self, nums):
#         heap = []
#         for num in nums:
#             tmp = num
#             while tmp%2 == 0: tmp//=2
#             heap.append((tmp, max(num, tmp*2)))
        
#         Max = max(i for i,j in heap)
#         heapify(heap)
#         ans = float("inf")

#         while len(heap) == len(nums):
#             num, limit = heappop(heap)
#             ans = min(ans, Max - num)
#             if num < limit:
#                 heappush(heap, (num*2, limit))
#                 Max = max(Max, num*2)
            
#         return ans