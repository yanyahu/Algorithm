# https://leetcode.com/problems/sort-list/

'''
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur = head
        old_list = []
        while cur:
            old_list.append(cur.val)
            cur = cur.next
        new_list = sorted(old_list)
        new_cur = new_head = ListNode(new_list[0])
        for i in new_list[1:]:
            new_cur.next = ListNode(i)
            new_cur = new_cur.next
        return new_head
