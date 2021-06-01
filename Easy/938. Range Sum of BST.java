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
    public int rangeSumBST(TreeNode root, int L, int R) {
        int res = 0;
        if(root == null){return 0;}
        if(root.val>= L && root.val<=R){res+=root.val;}
        return res+rangeSumBST(root.right,L,R)+rangeSumBST(root.left,L,R);
    }
}


/*  Runtime: 1 ms, faster than 53.67% of Java online submissions for Range Sum of BST.
Memory Usage: 48.5 MB, less than 62.21% of Java online submissions for Range Sum of BST.
 */