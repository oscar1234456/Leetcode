# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = list()
        q = deque()
        if not root:
            return res
        q.append(root)
        
        while len(q)!=0:
            res.append(q[len(q)-1].val)
            for i in range(len(q)):
                temp = q.popleft()
                if temp.left: q.append(temp.left)
                if temp.right: q.append(temp.right)
        return res
        
        