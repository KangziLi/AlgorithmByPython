# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:05:11 2017

@author: KangziLi
@source: lintcode - 141. Sqrt(x)
"""

class Solution:
    """
    @param: x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        start, end = 1, x
        while start + 1< end:
            mid = (start + end) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid
            else:
                end = mid
        return min(start,end)