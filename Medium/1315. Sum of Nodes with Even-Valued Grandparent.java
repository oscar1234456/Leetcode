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
    public int sumEvenGrandparent(TreeNode root) {
        int rootVal = root.val;
        if(rootVal%2==0){
            return countEven(root.left,true,false)+countEven(root.right,true,false);
        }
        return countEven(root.left,false,false)+countEven(root.right,false,false);
    }

    private int countEven(TreeNode node,boolean isParentEven,boolean isGrandEven){
        if (node == null){return 0;}
        int addCount = 0;
        if(isGrandEven == true){addCount+=node.val;}

        boolean isSelfEven = false;
        if(node.val % 2 == 0 ){isSelfEven = true;}

        return addCount+countEven(node.left,isSelfEven,isParentEven)+countEven(node.right,isSelfEven,isParentEven);
    }

}

/* Runtime: 1 ms, faster than 99.58% of Java online submissions for Sum of Nodes with Even-Valued Grandparent.
Memory Usage: 43.1 MB, less than 100.00% of Java online submissions for Sum of Nodes with Even-Valued Grandparent. in a Sorted Matrix.
 */