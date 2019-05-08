# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = my_cur = ListNode(0)
        l1_cur, l2_cur = l1, l2
        num = 0
        while l1_cur or l2_cur or num:
            if l1_cur:
                num += l1_cur.val
                l1_cur = l1_cur.next
            if l2_cur:
                num += l2_cur.val
                l2_cur = l2_cur.next
            my_cur.next = ListNode(num % 10)
            my_cur = my_cur.next
            num //= 10    
        return head.next