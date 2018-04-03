# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 00:18:59 2018

@author: Kangzi Li

LeetCode:606. Construct String from Binary Tree
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        res = ''
        if not t:
            return res
        res = str(t.val)
        if t.left:
            res += '('+self.tree2str(t.left)+')'
            if t.right:
                res += '('+self.tree2str(t.right)+')'
        elif t.right:
            res += '()'+'('+self.tree2str(t.right)+')'
        return res
#    def tree2str(self, t):
#        if not t: return ''
#        left = '({})'.format(self.tree2str(t.left)) if (t.left or t.right) else ''
#        right = '({})'.format(self.tree2str(t.right)) if t.right else ''
#        return '{}{}{}'.format(t.val, left, right)