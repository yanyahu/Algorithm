#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        new_cur_1 = new_head_1 = ListNode(0)
        new_cur_2 = new_head_2 = ListNode(0)
        while head:
            if head.val < x:
                new_cur_1.next = head
                new_cur_1 = new_cur_1.next
            else:
                new_cur_2.next = head
                new_cur_2 = new_cur_2.next
            head = head.next
        new_cur_2.next = None
        new_cur_1.next = new_head_2.next
        return new_head_1.next
