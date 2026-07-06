# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = dummy

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                prev.next = list1
                prev = prev.next
                list1 = list1.next
            else:
                prev.next = list2
                prev = prev.next
                list2 = list2.next
        
        remainder = None
        if list1 != None:
            remainder = list1
        else:
            remainder = list2
        
        while remainder != None:
            prev.next = remainder
            prev = prev.next
            remainder = remainder.next


        return dummy.next