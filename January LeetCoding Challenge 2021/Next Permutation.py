class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last = -1
        iout = -1
        jout = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<last:
                #find stop point
                iout = i
                for j in range(len(nums)-1,i,-1):
                    if nums[j]>nums[i]:
                        nums[i],nums[j] = nums[j],nums[i]
                        break
                break
            else:
                #update last
                last = nums[i]
        # print(iout," ",jout)
        # print(nums)
        # self.reverse(nums, iout+1)
        i = iout+1
        j = len(nums)-1
        while(i<j):
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1
        
    # def reverse(self,nums,start):
    #     i = start
    #     j = len(nums)-1
    #     while(i<j):
    #         nums[i],nums[j] = nums[j],nums[i]
    #         i+=1
    #         j-=1
    
#1234
#1243
#1324
#1342
#1423
#1432
#2134
# ...
# 1.from right to left, find stop point i (begin not ascending)
# 2.if there is stop point, then find the first large number a[j] than n[i] in[i+1:len(n)].
# 3.swap(i, j)
# 4.[i+1:len(n)] sort
# About sort:
# we can use reverse elements to deal with [i+1:len(n)]