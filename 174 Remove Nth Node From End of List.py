# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 13:45:34 2017

@author: KangziLi
@source: lintcode - 174. Remove Nth Node From End of List
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
    @param: head: The first node of linked list.
    @param: n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        res = ListNode(0)
        res.next = head
        tmp = res
        for i in range(n):
            head = head.next
        while head!=None:
            head = head.next
            tmp = tmp.next
        tmp.next = tmp.next.next
        return res.next
