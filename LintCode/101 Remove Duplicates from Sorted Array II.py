# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:35:29 2017

@author: KangziLi
@source: lintcode - 101. Remove Duplicates from Sorted Array II
"""

class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        if len(nums) < 2:
            return len(nums)
        res = []        
        before = None
        count = 0
        for i in nums:
            if before != i:
                res.append(i)
                before = i
                count = 1
            elif count<2:
                res.append(i)
                count+=1
        for r in range(len(res)):
            nums[r]=res[r]
        return len(res)
            