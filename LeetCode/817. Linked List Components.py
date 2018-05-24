#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 16:36:46 2018

@author: Kangzi Li

LeetCode: 817. Linked List Components
"""

#We are given head, the head node of a linked list containing unique integer values.
#
#We are also given the list G, a subset of the values in the linked list.
#
#Return the number of connected components in G, where two values are connected 
#if they appear consecutively in the linked list.
#
#Input: 
#head: 0->1->2->3->4
#G = [0, 3, 1, 4]
#Output: 2
#Explanation: 
#0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two
# connected components.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        gset = set(G)
        cur = head
        ans = 0
        while cur:
            if cur.next:
                nextval = cur.next.val
            else:
                nextval = None
            if cur.val in gset and nextval not in gset:
                ans += 1             
            cur = cur.next
        return ans
        











