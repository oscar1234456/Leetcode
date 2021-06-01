# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        
        turtle = head
        rabbit = head
        
        turtle = turtle.next
        rabbit = rabbit.next
        if rabbit:
            rabbit = rabbit.next
        
        while turtle != rabbit and rabbit:
            print("turtle != rabbit")
            turtle = turtle.next
            rabbit = rabbit.next
            if rabbit:
                rabbit = rabbit.next
        
        if rabbit:
            # have cycle
            turtle = head
            # while turtle!=rabbit:
            #     print("in")
            #     turtle = turtle.next
            #     rabbit = rabbit.next
            # print(turtle.val)
            return True
        else:
            #not have cycle
            return False


# Floyd Cycle Detection Algorithm (Tortoise and Hare Algorithm)
#beats 90.2%