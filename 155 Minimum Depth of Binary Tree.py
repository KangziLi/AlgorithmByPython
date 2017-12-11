# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:05:06 2017

@author: KangziLi
@source: lintcode - 155. Minimum Depth of Binary Tree
"""

#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    Given a binary tree, find its minimum depth.
    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
    @param: root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        if root is None:
            return 0
        left, right = 0, 0
        if root.left != None:
            left = self.minDepth(root.left)
        else:
            return self.minDepth(root.right)+1
        if root.right != None:
            right = self.minDepth(root.right)
        else:
            return left +1
        return min(left,right)+1