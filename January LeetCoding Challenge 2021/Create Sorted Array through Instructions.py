# Solution1 Time Exceed!
# from collections import defaultdict
# import bisect
# class Solution:
#     def createSortedArray(self, instructions: List[int]) -> int:
#         cost = 0
#         a = []
#         length = 0
#         countDict = defaultdict(self.zero)
#         for i in instructions:
#             left = bisect.bisect_left(a,i)
#             a.insert(left,i)
#             # countDict[i] += 1 
#             length += 1
#             # right = length-left-countDict[i]
#             right = length-bisect.bisect_right(a,i)
#             cost += min(left, right)
#         return cost % (10**9 + 7)
    
#     def zero(self):
#         return 0

from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions):
        SList = SortedList()
        ans = 0
        for num in instructions:
            ans += min(SList.bisect_left(num), len(SList) - SList.bisect_right(num))
            ans %= (10**9 + 7)
            SList.add(num)

        return ans

            