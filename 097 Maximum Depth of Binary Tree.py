# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 21:29:36 2017

@author: KangziLi
@source: lintcode - 97. Maximum Depth of Binary Tree
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    Given a binary tree, find its maximum depth.
    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    @param root: The root of binary tree.
    @return: An integer
    """ 
    def maxDepth(self, root):
        if root is None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
            
            
            