# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 00:28:12 2017

@author: KangziLi
@source: lintcode - 166. Nth to Last Node in List
"""

#Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param: head: The first node of linked list.
    @param: n: An integer
    @return: Nth to last node of a singly linked list. 
    """
    def nthToLast(self, head, n):
        if head is None or n<1:
            return None
        p = head
        q = head
        for i in range(n-1):
            if p == None:
                return None
            p = p.next
        while p.next != None:
            q = q.next
            p = p.next
        return q
