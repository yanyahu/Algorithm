# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur = self
        have_set = set()
        while head:
            if head.val not in have_set:
                cur.next = ListNode(head.val)
                cur = cur.next
                have_set.add(head.val)
            head = head.next
        return self.next
