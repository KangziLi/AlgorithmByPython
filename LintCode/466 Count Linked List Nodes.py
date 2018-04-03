# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 09:02:47 2017

@author: KangziLi
@source: lintcode - 466. Count Linked List Nodes
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
    Count how many nodes in a linked list.
    @param: head: the first node of linked list.
    @return: An integer
    """
    def countNodes(self, head):
        if head is None:
            return 0
        count = 1 
        while head:
            if head.next is None:
                return count
            head = head.next
            count += 1