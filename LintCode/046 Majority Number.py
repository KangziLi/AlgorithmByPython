# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 21:50:53 2017

@author: KangziLi
@source: lintcode - 46. Majority Number
"""

class Solution:
    """
    Given an array of integers, the majority number is the number that occurs more than half of the size of the array. Find it.
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            elif candidate == num:
                count += 1
            else:
                count -= 1
        return candidate