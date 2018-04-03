# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 23:03:21 2017

@author: KangziLi
@source: lintcode - 452. Remove Linked List Elements
"""

"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""

class Solution:
    """
    Remove all elements from a linked list of integers that have value val.
    @param: head: a ListNode
    @param: val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        if head is None:
            return head
        temp1 = ListNode(0)
        temp1.next = head
        temp2 = temp1
        while head:
            if head.val == val:
                temp2.next = head.next
                head = temp2
            temp2 = head
            head = head.next
        return temp1.next
            