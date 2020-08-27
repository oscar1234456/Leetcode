# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None: return None
        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
        
# Runtime: 80 ms, faster than 74.05% of Python3 online submissions for Search in a Binary Search Tree.
# Memory Usage: 15.5 MB, less than 98.58% of Python3 online submissions for Search in a Binary Search Tree.