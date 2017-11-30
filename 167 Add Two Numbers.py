# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:08:57 2017

@author: KangziLi
@source: lintcode - 167. Add Two Numbers
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
    You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
    @param: l1: the first list
    @param: l2: the second list
    @return: the sum list of l1 and l2 
    """
    def addLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = ListNode(0)
        temp = head
        carry = 0
        while True:
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            temp.val = carry % 10
            carry /= 10
            if l1 != None or l2!= None or carry !=0:
                temp.next = ListNode(0)
                temp = temp.next
            else:
                break
        return head
