# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 23:47:57 2017

@author: KangziLi
@source: lintcode - 44. Minimum Subarray
"""

class Solution:
    """
    Given an array of integers, find the subarray with smallest sum.
    Return the sum of the subarray.
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        sum = 0
        minsum = nums[0]
        maxsum = 0
        for num in nums:
            sum += num
            if sum-maxsum<minsum:
                minsum = sum - maxsum
            if sum>maxsum:
                maxsum = sum
        return minsum