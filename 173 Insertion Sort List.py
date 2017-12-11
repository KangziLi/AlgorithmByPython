# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 13:45:07 2017

@author: KangziLi
@source: lintcode - 173. Insertion Sort List
"""

#Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param: head: The first node of linked list.
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        temp = ListNode(0)
        while head:
            t1 = temp
            t2 = head.next
            while t1.next and t1.next.val < head.val:
                t1= t1.next
            head.next = t1.next
            t1.next = head
            head = t2
        return temp.next
            
