# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 22:12:50 2017

@author: KangziLi
@source: lintcode - 165. Merge Two Sorted Lists
"""


Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Merge two sorted (ascending) linked lists and return it as a new sorted list. The new sorted list should be made by splicing together the nodes of the two lists and sorted in ascending order.
    @param: l1: ListNode l1 is the head of the linked list
    @param: l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = ListNode(0)
        res = head
        while l1!=None and l2 != None:
            if l1.val <l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 =l2.next
            res = res.next
        if l1 != None:
            res.next=l1
        else:
            res.next=l2
        return head.next
        
    
        