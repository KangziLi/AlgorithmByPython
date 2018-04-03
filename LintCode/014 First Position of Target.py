# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 10:01:22 2017

@author: KangziLi
@source: lintcode - 14. First Position of Target
"""

class Solution:
    """
    For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.
    If the target number does not exist in the array, return -1.
    @param nums: The integer array
    @param target: Target number to find
    @return the first position of target in nums, position start from 0
    """
    def binarySearch(self, nums, target):  
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1