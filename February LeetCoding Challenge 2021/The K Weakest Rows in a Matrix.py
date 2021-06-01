class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldierNum = list()
        res = list()
        for row in mat:
            count = 0
            for item in row:
                if item == 1:
                    count+=1
                    continue
                
            soldierNum.append(count)
            
        while k>0:
            maxItem =  99999
            maxIndex = -1
            for i in range(len(soldierNum)):
                if soldierNum[i] < maxItem:
                    maxItem = soldierNum[i]
                    maxIndex = i
            soldierNum[maxIndex] = 99999
            res.append(maxIndex)
            k-=1
        return res
#Solution2 (faster than first)
# from collections import defaultdict
# class Solution:
#     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#         keep = defaultdict(list)
#         res = list()
#         i = 0
#         for row in mat:
#             count = 0
#             for item in row:
#                 if item == 1:
#                     count+=1
#                 else:
#                     break
#             keep[count].append(i)
#             i+=1
#         for i in sorted(keep.keys()):
#             if k==0: break
#             for item in keep[i]:
#                 res.append(item)
#                 k-=1
#                 if k==0: break
#         return res
        

#solution3: (other people)
# class Solution:
#     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#         d = {}
        
#         for i in range(len(mat)):
#             d[i] = sum(mat[i])
        
#         return sorted(d, key=d.get)[:k]