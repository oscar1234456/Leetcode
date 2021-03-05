# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Solution 1 : Time limit exceed (O(M*N))
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        nodeB = headB
        nodeA = headA
        
        while nodeB!=None:
            while nodeA != None:
                if nodeB == nodeA:
                    return nodeB
                nodeA = nodeA.next
            nodeB = nodeB.next
            nodeA = headA
        return None


# Solution 2 : Accepted (O(M+N)), Hash Table
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        nodeB = headB
        nodeA = headA
        temp = set()
       
        while nodeB!=None:
            temp.add(nodeB)
            nodeB = nodeB.next
        
        while nodeA!=None:
            if nodeA in temp:
                return nodeA
            nodeA = nodeA.next
        return None
        
      