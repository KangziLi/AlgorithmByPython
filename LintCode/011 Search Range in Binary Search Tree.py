# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 22:26:21 2017

@author: KangziLi
@source: lintcode - 11. Search Range in Binary Search Tree
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
    Given two values k1 and k2 (where k1 < k2) and a root pointer to a Binary Search Tree. Find all the keys of tree in range k1 to k2. i.e. print all x such that k1<=x<=k2 and x is a key of given BST. Return all the keys in ascending order.
    @param: root: param root: The root of the binary search tree
    @param: k1: An integer
    @param: k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        if root is None:
            return []
        res = []
        queue = [root]
        i=0
        while i < len(queue):
            if queue[i] is not None:
                if queue[i].val >=k1 and queue[i].val<=k2:
                    res.append(queue[i].val)
                queue.append(queue[i].left)
                queue.append(queue[i].right)
            i += 1
        return sorted(res)
        