# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        self.nums = []
        self.nodes = []
        self.inorder(root)
        self.sortnum = sorted(self.nums)        
        
        for i in range(len(self.nums)):
            if self.nums[i] != self.sortnum[i]:
                self.nodes[i].val = self.sortnum[i]
        
        
    def inorder(self,node: TreeNode):
        if node == None:
            return
        
        self.inorder(node.left)
        self.nums.append(node.val)
        self.nodes.append(node)
        self.inorder(node.right)

"""
Runtime: 68 ms, faster than 84.73% of Python3 online submissions for Recover Binary Search Tree.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Recover Binary Search Tree.
"""