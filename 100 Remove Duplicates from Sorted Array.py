# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 09:37:17 2017

@author: KangziLi
@source: lintcode - 100. Remove Duplicates from Sorted Array
"""

class Solution:
    """
    Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
    Do not allocate extra space for another array, you must do this in place with constant memory.
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        if len(nums)<2:
            return len(nums)
        index = 0
        for i in range(1, len(nums)):
            if nums[index] != nums[i]:
                index += 1
                nums[index] = nums[i]
        return index + 1
        
        
