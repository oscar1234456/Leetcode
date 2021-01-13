# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i = l1
        j = l2
        l1Keep = True
        l2Keep = True
        root = ListNode()
        z = root
        while True:
            carry = 0
            if i != None:
                z.val += i.val
                i = i.next
                
            if j != None:
                z.val += j.val
                j = j.next
               
            if  (i == None ) and   (j == None):
                if z.val >= 10:
                    carry = z.val // 10
                    z.val = z.val % 10
                    z.next = ListNode()
                    z = z.next
                    z.val += carry
                return root
            else:
                if z.val >= 10:
                    carry = z.val // 10
                    z.val = z.val % 10
                z.next = ListNode()
                z = z.next
                z.val += carry
                
        
        
        
        
            