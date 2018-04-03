# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 16:39:40 2017

@author: KangziLi
@source: lintcode - 93. Balanced Binary Tree
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
    Given a binary tree, determine if it is height-balanced.
    For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
    @param: root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
       balanced, _ = self.validate(root)
       return balanced
   
    def validate(self, root):
        if root is None:
            return True, 0
        balanced, leftHeight = self.validate(root.left)
        if not balanced:
            return False,0
        balanced, rightHeight = self.validate(root.right)
        if not balanced:
            return False,0
        return abs(leftHeight - rightHeight)<=1, max(leftHeight,rightHeight)+1
        