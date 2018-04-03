# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:59:31 2017

@author: KangziLi
@source: lintcode - 452. Remove Linked List Elements
"""

class Solution:
    """
    Find the maximum node in a binary tree, return the node.
    @param: root: the root of tree
    @return: the max node
    """
    def maxNode(self, root):
        if root is None:
            return root
        left = self.maxNode(root.left)
        right = self.maxNode(root.right)
        return self.max(root, self.max(left,right))
    
    def max(self, x, y):
        if x is None:
            return y
        if y is None:
            return x
        if x.val > y.val:
            return x
        return y