"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None

        # Make a copy of the linked list without random pointers
        new = []
        original = []
        mapping = {None: None}
        while head:
            original.append(head)
            new.append(Node(head.val))
            if len(new) > 1:
                new[-2].next = new[-1]
            mapping[head] = new[-1]
            head = head.next

        # set random pointers in new linked list
        for i in range(len(new)):
            new[i].random = mapping[original[i].random]

        return new[0]