class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        freq = Counter(nums)
        max_len = 0
        
        for elem in freq:
            if elem-1 in freq:
                possible_max1 = freq[elem] + freq[elem-1]
                max_len = possible_max1 if possible_max1 > max_len else max_len
            
            elif elem+1 in freq:
                possible_max2 = freq[elem] + freq[elem+1]
                max_len = possible_max2 if possible_max2 > max_len else max_len
        
        return max_len