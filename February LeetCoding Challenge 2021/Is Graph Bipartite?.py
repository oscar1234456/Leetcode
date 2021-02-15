import queue
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0 for _ in range(len(graph))]
        #Label1:Red
        #Label2:Green
        
        for i in range(len(graph)):
            if visited[i] != 0:
                continue
            
            q = queue.Queue()
            q.put(i)
            visited[i] = 1
            
            while not q.empty():
                now = q.get()
                nowColor = visited[now]
                neighborColor = 2 if nowColor==1 else 1
                
                for neighbor in graph[now]:
                    if visited[neighbor] == 0:
                        visited[neighbor] = neighborColor
                        q.put(neighbor)
                    elif visited[neighbor]!=neighborColor:
                        return False
            
        return True
                        
            