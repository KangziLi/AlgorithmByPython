#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 16:09:15 2018

@author: Kangzi Li

LeetCode: 515. Find Largest Value in Each Tree Row
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        maxs = []
        queue = [root]
        if not root:
            return maxs
        while len(queue):
            maxs.append(max(n.val for n in queue))
            queue = [kid for node in queue for kid in (node.left,node.right) if kid]
        return maxs
            
            
