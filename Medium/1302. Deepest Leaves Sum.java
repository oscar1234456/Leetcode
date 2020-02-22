/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    int maxHeight = 0;
    public int deepestLeavesSum(TreeNode root) {
        maxHeight = maxHeight(root);
        if(root.left == null && root.right == null){return root.val;}
        return helper(root.left,1)+helper(root.right,1);
    }

    public int maxHeight(TreeNode node){
        if(node == null){return 0;}
        return Math.max(maxHeight(node.left),maxHeight(node.right))+1;
    }
    public int helper(TreeNode node, int nowLevel){
        if(node == null){return 0;}
        nowLevel++;
        if(nowLevel == maxHeight){return node.val;}
        return helper(node.left,nowLevel)+helper(node.right,nowLevel);
    }
}
/*
Runtime: 1 ms, faster than 93.93% of Java online submissions for Deepest Leaves Sum.
Memory Usage: 43.2 MB, less than 100.00% of Java online submissions for Deepest Leaves Sum.
 */