# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#note:
#使用前序
#有點像bt compare, bt copy
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None and t2 is None: return None
        elif t1 is None:
            #t2 is not None
            t = TreeNode(t2.val)
            t.left = self.mergeTrees(None, t2.left)
            t.right = self.mergeTrees(None,t2.right)
           
        elif t2 is None:
            #t1 is not None
            t = TreeNode(t1.val)
            t.left = self.mergeTrees(t1.left, None)
            t.right = self.mergeTrees(t1.right, None)
        else:
            #t1,t2 are not None
            t = TreeNode(t1.val+t2.val)
            t.left = self.mergeTrees(t1.left, t2.left)
            t.right = self.mergeTrees(t1.right, t2.right)
        return t

# Runtime: 108 ms, faster than 48.37% of Python3 online submissions for Merge Two Binary Trees.
# Memory Usage: 14.8 MB, less than 70.18% of Python3 online submissions for Merge Two Binary Trees.