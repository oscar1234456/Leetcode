# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q = queue.Queue()
        res = list()
        
        # res.append(root.val)
        q.put(root)
        size = q.qsize()
        
        temp = 0
        num = 1
        while size > 0:
            now = q.get()
            temp+=now.val
            if now.left:
                q.put(now.left)
            if now.right:
                q.put(now.right)
            size-=1
            if size==0:
                temp/=num
                res.append(temp)
                temp = 0
                size=q.qsize()
                num = size
        return res