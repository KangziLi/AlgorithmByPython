# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:14:11 2017

@author: KangziLi
@source: lintcode - 69. Binary Tree Level Order Traversal
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
    Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
    @param: root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        if root is None:
            return []
        res = []
        stack = [root]
        while stack:
            newstack = []
            res.append([i.val for i in stack])
            for node in stack:
                if node.left:
                    newstack.append(node.left)
                if node.right:
                    newstack.append(node.right)
            stack = newstack
        return res