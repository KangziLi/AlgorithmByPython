#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 15:56:19 2018

@author: Kangzi Li

LeetCode: 513. Find Bottom Left Tree Value
"""


#Given a binary tree, find the leftmost value in the last row of the tree.

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        for node in queue:
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val