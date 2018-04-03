# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 00:11:04 2018

@author: Kangzi Li

LeetCode:653. Two Sum IV - Input is a BST
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        bsf,s =[root],set()
        for i in bsf:
            if (k-i.val) in s:
                return True
            s.add(i.val)
            if i.left:
                bsf.append(i.left)
            if i.right:
                bsf.append(i.right)
        return False
            
        