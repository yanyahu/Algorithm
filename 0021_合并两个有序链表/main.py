#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
            常规解法
        '''
        l = ListNode(0)
        cur = l
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        else:
            cur.next = l2
        return l.next
"""


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
            递归解法
        """
        if not l1:
            return l2
        if not l2:
            return l1

        start = None
        if l1.val < l2.val:
            start = l1
            start.next = self.mergeTwoLists(l1.next, l2)
        else:
            start = l2
            start.next = self.mergeTwoLists(l1, l2.next)

        return start
