/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int getDecimalValue(ListNode head) {
        StringBuilder res = new StringBuilder();
        ListNode node = head;
        do{
            res.append(node.val);
            node = node.next;
        }while(node!=null);

        return Integer.parseInt(res.toString(),2);
    }
}


/*  Runtime: 0 ms, faster than 100.00% of Java online submissions for Convert Binary Number in a Linked List to Integer.
Memory Usage: 37.1 MB, less than 100.00% of Java online submissions for Convert Binary Number in a Linked List to Integer.
 */