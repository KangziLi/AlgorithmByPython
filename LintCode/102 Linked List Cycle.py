# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 17:31:05 2017

@author: KangziLi
@source: lintcode - 102. Linked List Cycle
"""

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    Given a linked list, determine if it has a cycle in it.
    @param: head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False