#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 17:25:30 2018

@author: Kangzi Li

LeetCode: 206. Reverse Linked List
"""

#Reverse a singly linked list.
#Input: 1->2->3->4->5->NULL
#Output: 5->4->3->2->1->NULL

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        prev = None
        cur = head
        post = cur.next
        while post:
            cur.next = prev
            prev = cur
            cur = post
            post = cur.next
        cur.next = prev
        return cur
            