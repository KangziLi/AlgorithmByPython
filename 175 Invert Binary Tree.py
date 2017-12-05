# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:54:47 2017

@author: KangziLi
@source: lintcode - 175. Invert Binary Tree
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
    Invert a binary tree.
    @param: root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        self.dfs(root)
    def dfs(self, node):
        left = node.left
        right = node.right
        node.left = right
        node.right = left
        if (left!=None): self.dfs(left)
        if (right!=None): self.dfs(right)
        