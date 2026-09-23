# https://leetcode.com/problems/add-two-numbers

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
        
        num2 = ""
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
        
        add_num = int(num1) + int(num2)
        add_num_str = str(add_num)[::-1]

        dummy = ListNode(0)
        curr = dummy
        for digit in add_num_str:
            curr.next = ListNode(int(digit))
            curr = curr.next
        
        return dummy.next