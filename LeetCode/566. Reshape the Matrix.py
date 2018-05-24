#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:52:26 2018

@author: Kangzi Li

LeetCode: 566. Reshape the Matrix
"""

#You're given a matrix represented by a two-dimensional array, and two positive 
#integers r and c representing the row number and column number of the wanted 
#reshaped matrix, respectively.
#
#The height and width of the given matrix is in range [1, 100].
#The given r and c are all positive.

#Input: 
#nums = [[1,2],[3,4]]
#r = 1, c = 4
#Output: 
#[[1,2,3,4]]

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r * c: return nums
        restemp, result = sum(nums,[]), []
        for i in range(0, r):
            result.append(restemp[c*i:c*(i+1)])
        return result
            
        
        
        
        