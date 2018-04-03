# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:10:03 2017

@author: KangziLi
@source: lintcode - 112. Remove Duplicates from Sorted List
"""

#Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param: head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        if head is None or head.next == None:
            return head
        res = ListNode(0)
        res = head
        while res.next:
            if res.val == res.next.val:
                res.next = res.next.next
            else:
                res = res.next
        return head
            
            