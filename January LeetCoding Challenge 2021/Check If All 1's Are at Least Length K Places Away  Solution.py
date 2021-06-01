#Solution1: 544ms
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = 0
        countable = False
        for i in nums:
            if not countable and i==1:
                countable = True
            elif i==1:
                #countable = True
                if count<k:
                    return False
                else:
                    count = 0
            elif countable:
                # i == 0
                count+=1
        return True

#Solution2: 536ms
# class Solution:
    # def kLengthApart(self, nums: List[int], k: int) -> bool:
    #     # initialize the counter of zeros to k
    #     # to pass the first 1 in nums
    #     count = k
        
    #     for num in nums:
    #         # if the current integer is 1
    #         if num == 1:
    #             # check that number of zeros in-between 1s
    #             # is greater than or equal to k
    #             if count < k:
    #                 return False
    #             # reinitialize counter
    #             count = 0
    #         # if the current integer is 0
    #         else:
    #             # increase the counter
    #             count += 1
                
    #     return True    
    # 
#Solution3: 912ms (Bit Manipulation)
# class Solution:
    # def kLengthApart(self, nums: List[int], k: int) -> bool:
    #     # convert binary array into int
    #     x = 0
    #     for num in nums:
    #         x = (x << 1) | num
        
    #     # base case
    #     if x == 0 or k == 0:
    #         return True
        
    #     # remove trailing zeros
    #     while x & 1 == 0:
    #         x = x >> 1
        
    #     while x != 1:
    #         # remove trailing 1-bit
    #         x = x >> 1
            
    #         # count trailing zeros
    #         count = 0
    #         while x & 1 == 0:
    #             x = x >> 1
    #             count += 1
                
    #         # number of zeros in-between 1-bits
    #         # should be greater than or equal to k
    #         if count < k:
    #             return False
        
    #     return True      