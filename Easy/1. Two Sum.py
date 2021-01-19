class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = dict()
        i=0
        for n in nums:
            if n in pair: #find pairs!
                return [pair[n], i]
            else:
                pair[target-n] = i
                i+=1

# Runtime: 36 ms, faster than 99.05% of Python3 online submissions for Two Sum.
# Memory Usage: 14.5 MB, less than 45.84% of Python3 online submissions for Two Sum.