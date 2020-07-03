# https://leetcode.com/problems/partition-list/

'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''

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
