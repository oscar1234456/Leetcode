import queue
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1
        directions = [(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1)]
        visited = [[False for _ in range(m)] for __ in range(n)]
        q = queue.Queue()
        q.put((0,0))
        count = 0
        
        while not q.empty():
            size = q.qsize()
            for i in range(size):
                now = q.get()
                if now==(m-1, n-1):
                    return count+1
                for direc in directions:
                    x = direc[0] + now[0]
                    y = direc[1] + now[1]
                    if x>=0 and x<m and y>=0 and y<n and grid[x][y]==0 and not visited[x][y]:
                        q.put((x, y))
                        visited[x][y] = True
            count+=1
        return -1
                        