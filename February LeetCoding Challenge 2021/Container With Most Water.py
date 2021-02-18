class Solution:
    def maxArea(self, height: List[int]) -> int:
        width = len(height)
        L = 0
        R = width-1
        res = 0
        for i in range(width-1, 0 ,-1):
            if height[L] < height[R]:
                res = max(res, height[L]*i)
                L = L+1
            else:
                res = max(res, height[R]*i)
                R = R-1
        return res