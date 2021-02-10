# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
                   
        def allTrave(node):
            if node==None:
                return 0
            cout = node.val
            cout += allTrave(node.left)
            cout += allTrave(node.right)
            return cout
        
        def travBST(new, rightLeft, node):
            if not node:
                return
            if node.right:
                node.val = allTrave(node.right)+new+node.val
                if rightLeft:
                    #right side
                    travBST(0,True,node.right)
                else:
                    #left side
                    travBST(new,False,node.right)
            if node.left:
                if node.right==None:
                    node.val = new+node.val
                travBST(node.val,False,node.left)
            if not node.right  and not node.left:
                node.val = new+node.val
                
        travBST(0,True,root)
        return root
        