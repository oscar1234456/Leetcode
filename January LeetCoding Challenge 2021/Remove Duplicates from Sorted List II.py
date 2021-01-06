# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        i = head
        j = head
        sameCounter = 1
        
        if i is None or j is None:
            return
        else:
            i_keep = i.val
            j = j.next
            if j.val != i_keep:
                #case 1
                pass
            else:
                #case2
                while sameCounter >= 1:
                    sameCounter = 0
                    
                    while j.next is not None:
                        j = j.next
                        if j.val == i_keep:
                            sameCounter += 1
                            # if j.next is None:
                            #     return  #最後一個也不符合
                        else:
                            # if j.next is None:
                            #     return  head
                            # else:
                            #     break
                            break
                    i = j
                    head = i
                    if j.next is None:
                        return head if j.val != i_keep else None
                    i_keep = i.val
                
                          
                        
                
                
                    
                        
                
        