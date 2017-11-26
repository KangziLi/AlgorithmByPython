"""
Created on Sun Nov 26 20:44:06 2017

@author: KangziLi
@source: lintcode - 35. Reverse Linked List
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
    Reverse a linked list.
    @param: head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        if head == None:
            return head
        newhead = None
        while head != None:
            temp = head.next
            head.next = newhead
            newhead = head
            head = temp
        return newhead