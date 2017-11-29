# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 23:59:28 2017

@author: KangziLi
@source: lintcode - 6. Merge Two Sorted Arrays
"""

class Solution:
    """
    Merge two given sorted integer array A and B into a new sorted integer array.
    @param: A: sorted integer array A
    @param: B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        A=A+B
        A.sort()
        return A