# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 00:15:24 2017

@author: KangziLi
@source: lintcode - 372. Delete Node in the Middle of Singly Linked List
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
    Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.
    @param: node: the node in the list should be deletedt
    @return: nothing
    """
    def deleteNode(self, node):
        if node is None or node.next is None:
            return 
        next = node.next
        node.val = next.val
        node.next = next.next
        return