# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 19:42:56 2018

@author: Kangzi Li

LeetCode:226. Invert Binary Tree
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 
        root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root