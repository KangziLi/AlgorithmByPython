# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:08:00 2017

@author: KangziLi
@source: lintcode - 68. Binary Tree Postorder Traversal
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
    Given a binary tree, return the postorder traversal of its nodes' values.
    @param: root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        if root is None:
            return []
        return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]