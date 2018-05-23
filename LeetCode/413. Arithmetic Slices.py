#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 15:07:40 2018

@author: Kangzi Li

LeetCode: 413. Arithmetic Slices
"""


#A zero-indexed array A consisting of N numbers is given. A slice of that array 
#is any pair of integers (P, Q) such that 0 <= P < Q < N.
#
#A slice (P, Q) of array A is called arithmetic if the sequence:
#A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means 
#that P + 1 < Q.
#
#The function should return the number of arithmetic slices in the array A.

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        dp = 0
        for i in range(1,len(A)-1):
            if A[i] - A[i-1] ==  A[i+1] - A[i]:
                dp += 1
                res += dp
            else:
                dp = 0
        return res
            