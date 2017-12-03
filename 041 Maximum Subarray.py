# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 21:45:09 2017

@author: KangziLi
@source: lintcode - 41. Maximum Subarray
"""

class Solution:
    """
    Given an array of integers, find a contiguous subarray which has the largest sum.
    @param: nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        local = nums[0]
        globa = nums[0]
        for i in range(1,len(nums)):
            local = max(local+nums[i],nums[i])
            globa = max(globa,local)
        return globa