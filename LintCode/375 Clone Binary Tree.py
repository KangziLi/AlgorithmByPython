# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:24:28 2017

@author: KangziLi
@source: lintcode - 375. Clone Binary Tree
"""

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None

class Solution:
    """
    @param: root: The root of binary tree
    @return: root of new tree
    """
    def cloneTree(self, root):
        if root is None:
            return None
        clone = TreeNode(root.val)
        clone.left = self.cloneTree(root.left)
        clone.right = self.cloneTree(root.right)
        return clone
