class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count = 0
        for i in range(1001):
            for j in nums:
                if i <= j:
                    count+=1
            if count == i:
                return count
            else:
                count = 0
        return -1
