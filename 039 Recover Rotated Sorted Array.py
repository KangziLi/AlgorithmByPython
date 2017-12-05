# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 23:47:10 2017

@author: KangziLi
@source: lintcode - 39. Recover Rotated Sorted Array
"""

class Solution:
    """
    Given a rotated sorted array, recover it to sorted array in-place.
    @param: nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        nums.sort()
