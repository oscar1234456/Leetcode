# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dic = defaultdict(list)
        visit = set()
        colPool = set()
        levelPool = set()
        res = list()
        self.preorder(dic, root, 0, 0)
        
        for i in dic:
            colPool.add(i[1])
            levelPool.add(i[0])

        for i in sorted(colPool):
            temp = []
            tt = [-1 for _ in range(len(levelPool))]
            for item in dic:
                if item[1]==i:
                    tt[item[0]] =  dic[item]
            for s in tt:
                if s!=-1:
                    temp+=s
            res.append(temp)
        return res
    
    def preorder(self, dic, node ,level, col):
        if node is None:
            return
        dic[(level,col)].append(node.val) #view
        dic[(level,col)].sort()
        self.preorder(dic, node.left, level+1, col-1) #left
        self.preorder(dic, node.right,level+1, col+1) #right
        
# Beats 80.48%