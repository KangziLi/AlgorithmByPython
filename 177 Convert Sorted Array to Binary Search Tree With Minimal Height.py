# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 13:45:31 2017

@author: KangziLi
@source: lintcode - 177. Convert Sorted Array to Binary Search Tree With Minimal Height
"""


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param: A: an integer array
    @return: A tree node
    """
    def sortedArrayToBST(self, A):
        return self.convert(A, 0, len(A)-1)
    
    def convert(self, A, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(A[start])
        mid = (start + end) / 2
        root = TreeNode(A[mid])
        root.left = self.convert(A,start,mid-1)
        root.right = self.convert(A,mid+1,end)
        return root