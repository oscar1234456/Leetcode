# my solution(faster than second solution)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = [i for i in range(1,2001)]
        diff = list((set(num)).difference(set (arr)))
        return diff[k-1]

# second solution
# class Solution:
    # def findKthPositive(self, arr: List[int], k: int) -> int:
    #     set_array = set(arr)
    #     for i in range(1, k+len(arr)+1):
    #         if i not in set_array: k-=1
    #         if k == 0: return i

# third solution (binary search)
# class Solution:
    # def findKthPositive(self, arr: List[int], k: int) -> int:
    #     beg = 0
    #     end = len(arr)
    #     while beg<end:
    #         mid  = (end+beg)//2
    #         if arr[mid]-mid-1 < k: #arr[mid]-i-1 means the number of lost number backward
    #             beg = mid+1
    #         else:
    #             end = beg
    #     return end+k