# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 19:37:33 2018

@author: Kangzi Li

LeetCode: 104. Maximum Depth of Binary Tree
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
             return 0
        return max(self.maxDepth(root.left)+1,self.maxDepth(root.right)+1)
        