# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None

        dummy = ListNode(0, head) 
        prev = dummy
        while head != None:
            check = head
            for i in range(n):
                check = check.next
            
            if check == None:
                prev.next = head.next
                head.next = None
                break

            prev = head
            head = head.next
                
        return dummy.next



    
                
                

        
        
        