# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        myStack = list()
        now = head
        ori = ""
        while now:
            myStack.append(str(now.val))
            ori += str(now.val)
            now = now.next
        
        stackLength = len(myStack)
        temp = ""
        for i in range(stackLength):
            temp += myStack.pop()
        
        if temp != ori:
            return False
        
        return True