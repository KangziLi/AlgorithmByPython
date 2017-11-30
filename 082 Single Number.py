# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:46:47 2017

@author: KangziLi
@source: lintcode - 82. Single Number
"""

class Solution:
    """
    Given 2*n + 1 numbers, every numbers occurs twice except one, find it.
    @param: A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        res = 0
        for x in A :
            res = res ^ x
        return res