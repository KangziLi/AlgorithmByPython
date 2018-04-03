# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 23:55:07 2017

@author: KangziLi
@source: lintcode - 50. Product of Array Exclude Itself
"""

class Solution:
    """
    Given an integers array A.
    Define B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1], calculate B WITHOUT divide operation.
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        length = len(nums)
        result = []
        f = [0]*length+[1]
        for i in range(length-1,0,-1):
            f[i]=f[i+1]*nums[i]
        tmp = 1
        for i in range(length):
            result.append(tmp*f[i+1])
            tmp *= nums[i]
        return result