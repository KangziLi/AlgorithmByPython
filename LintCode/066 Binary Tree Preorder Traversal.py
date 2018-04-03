# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:35:56 2017

@author: KangziLi
@source: lintcode - 66. Binary Tree Preorder Traversal
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
    Given a binary tree, return the preorder traversal of its nodes' values.
    @param: root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    
    def preorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        preorder = []
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder
        