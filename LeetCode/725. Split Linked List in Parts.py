#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 16:59:00 2018

@author: Kangzi Li

LeetCode: 725. Split Linked List in Parts
"""

#Given a (singly) linked list with head node root, write a function to split the 
#linked list into k consecutive linked list "parts".
#
#The length of each part should be as equal as possible: no two parts should have 
#a size differing by more than 1. This may lead to some parts being null.
#
#The parts should be in order of occurrence in the input list, and parts occurring 
#earlier should always have a size greater than or equal parts occurring later.
#
#Return a List of ListNode's representing the linked list parts that are formed.
#
#Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        cur = root
        n = 0
        while cur:
            n += 1
            cur = cur.next
        width, remainder = divmod(n,k)
        ans = []
        cur = root
        for i in range(k):
            head = cur
            for j in range(width + (i<remainder)-1):
                if cur:
                    cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            ans.append(head)
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        