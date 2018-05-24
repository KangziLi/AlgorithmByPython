#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 17:51:51 2018

@author: Kangzi Li

LeetCode: 445. Add Two Numbers II
"""


#You are given two non-empty linked lists representing two non-negative integers.
# The most significant digit comes first and each of their nodes contain a single
# digit. Add the two numbers and return it as a linked list.
#
#You may assume the two numbers do not contain any leading zero, except the number
# 0 itself.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        val1, val2 = 0, 0
        while l1:
            val1 = l1.val + val1 * 10
            l1 = l1.next
        while l2:
            val2 = l2.val + val2 * 10
            l2 = l2.next
        sum = val1 + val2
        head = ListNode(0)
        while sum:
            v = sum % 10
            sum /= 10
            head.val = v
            node = ListNode(sum)
            node.next = head
            head = node
        return head.next if(val1 + val2) !=0 else head
    
          
            
        
        
#        s1 = []
#        s2 = []
#        while l1 != None:
#            s1.append(l1.val)
#            l1 = l1.next
#        while l2 != None:
#            s2.append(l2.val)
#            l2 = l2.next
#        sum = 0
#        reslist = ListNode(0)
#        while len(s1) or len(s2):
#            if len(s1) != 0:
#                sum += s1.pop()
#            if len(s2) != 0:
#                sum += s2.pop()
#            reslist.val = sum %10
#            head = ListNode(int(sum/10))
#            head.next = reslist
#            reslist = head
#            sum = int(sum/10)
#        if reslist.val == 0:
#            return reslist.next
#        else:
#            reslist

            