#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 11:22:53 2018

@author: Kangzi Li

LeetCode: 561. Array Partition I
"""

# Given an array of 2n integers, your task is to group these integers into n 
# pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of 
# min(ai, bi) for all i from 1 to n as large as possible.
#
# n is a positive integer, which is in the range of [1, 10000].
# All the integers in the array will be in the range of [-10000, 10000].

# Input: [1,4,3,2]
# Output: 4

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum = 0
        for i in range(0,len(nums),2):
            sum += nums[i]
        return sum