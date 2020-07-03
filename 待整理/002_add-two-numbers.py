# https://leetcode.com/problems/add-two-numbers/

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

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