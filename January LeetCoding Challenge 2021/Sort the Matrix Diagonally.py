from collections import defaultdict
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        keep = defaultdict(list)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                keep[i-j].append(mat[i][j])
                
        for k in keep:
            keep[k].sort()
            
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = keep[i-j].pop(0)
        
        return mat
# Dict + sort beats 6.92%
