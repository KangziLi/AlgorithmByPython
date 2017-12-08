# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 21:38:35 2017

@author: KangziLi
@source: lintcode - 80. Median
"""

class Solution:
    """
    Given a unsorted array with integers, find the median of it.
    A median is the middle number of the array after it is sorted.
    If there are even numbers in the array, return the N/2-th number after sorted.   
    @param: : A list of integers
    @return: An integer denotes the middle number of the array
    """
    def median(self, nums):
        nums.sort()
        l = len(nums)
        k = int(l/2)
        if l%2 == 1:
            return nums[k]
        else:
            return nums[k-1]
