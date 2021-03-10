# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        q = queue.Queue()
        
        if d==1:
            newNode = TreeNode(v, root)
            return newNode
        elif d==2:
            root.left = TreeNode(v, root.left)
            root.right = TreeNode(v, right=root.right)
            return root
        
        q.put(root)
        i = d-2
        while i>0:
            nextSize = q.qsize()
            while nextSize > 0:
                now = q.get()
                if now.left:
                    q.put(now.left)        
                if now.right:
                    q.put(now.right)
                nextSize-=1
            i-=1
        size = q.qsize()
        # print(size)
        while size>0:
            now = q.get()
            now.left = TreeNode(v, now.left)
            now.right = TreeNode(v, right = now.right)
            size-=1
        
        return root
            