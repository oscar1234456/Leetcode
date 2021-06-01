class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        typeCount = len(set(candyType))
        
        return min(typeCount, len(candyType)//2)