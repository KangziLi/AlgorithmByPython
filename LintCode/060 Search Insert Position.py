# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 21:32:24 2017

@author: KangziLi
@source: lintcode - 60. Search Insert Position
"""

class Solution:
    """
    Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        if len(A) == 0:
            return 0
        start = 0
        end = len(A)-1
        while start+1<end:
            mid = (start + end) / 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        return len(A)
        