# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 16:17:56 2018

@author: Kangzi Li

LeetCode: 669. Trim a Binary Search Tree
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if L>root.val:
            return self.trimBST(root.right,L,R)
        if R<root.val:
            return self.trimBST(root.left,L,R)
        root.left = self.trimBST(root.left,L,R)
        root.right =self.trimBST(root.right,L,R)
        return root