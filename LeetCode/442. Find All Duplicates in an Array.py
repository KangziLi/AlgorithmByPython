#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 14:54:23 2018

@author: Kangzi Li

LeetCode: 442. Find All Duplicates in an Array
"""

#Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements 
#appear twice and others appear once.
#Find all the elements that appear twice in this array.
#Could you do it without extra space and in O(n) runtime?
#
#Input:
#[4,3,2,7,8,2,3,1]
#Output:
#[2,3]

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
            if nums[abs(nums[i])-1] > 0:
                res.append(abs(nums[i]))
        return res