# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1Pointer = l1
        l2Pointer = l2
        root = None
        nowPointer = root
        
        while True:
            if l1Pointer is None and l2Pointer is None:
                #case 1
                return None
            elif l2Pointer is None:
                #case 2
                if nowPointer is not None:
                    nowPointer.next = l1Pointer
                else:
                    root = l1Pointer
                return root
            
            elif l1Pointer is None:
                #case 3
                if nowPointer is not None:
                    nowPointer.next = l2Pointer
                else:
                    root = l2Pointer
                return root
            else:
                if l1Pointer.val <= l2Pointer.val:
                    newNode = ListNode(l1Pointer.val)
                    if nowPointer is None:
                        root = newNode
                        nowPointer = root
                        l1Pointer = l1Pointer.next
                    else:
                        nowPointer.next = newNode
                        nowPointer = nowPointer.next
                        l1Pointer = l1Pointer.next
                else:
                    newNode = ListNode(l2Pointer.val)
                    if nowPointer is None:
                        root = newNode
                        nowPointer = root
                        l2Pointer = l2Pointer.next
                    else:
                        nowPointer.next = newNode
                        nowPointer = nowPointer.next
                        l2Pointer = l2Pointer.next
                
            