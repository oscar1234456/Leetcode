class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        elementsNum = m*n
        if elementsNum != (r*c):
            return mat
        else:
            reshape = [[0 for _ in range(c)] for __ in range(r)]
            
            now = 0
            
            for i in range(r):
                for j in range(c):
                    reshape[i][j] = mat[now//n][now%n]
                    now += 1
            
            return reshape


#Solution 2:
# class Solution:
#     def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
#         result = [element for row in mat for element in row]
#         if len(result)==r*c:
#             return [result[i*c:(i+1)*c] for i in range(r)]
#         else:
#             return mat