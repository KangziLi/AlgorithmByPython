# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:24:25 2017

@author: KangziLi
@source: lintcode - 373. Partition Array by Odd and Even
"""

class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        if len(nums)<2:
            return
        start, end = 0, len(nums)-1
        while start < end:
            while start < end and nums[start]%2 == 1:
                start += 1
            while start < end and nums[end]%2 == 0:
                end -= 1
            if start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
                
