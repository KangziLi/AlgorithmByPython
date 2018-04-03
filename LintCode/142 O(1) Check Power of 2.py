# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:03:21 2017

@author: KangziLi
@source: lintcode - 142. O(1) Check Power of 2
"""

class Solution:
    """
    @param: n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        ans = 1
        for i in range(31):
            if ans == n:
                return True
            ans = ans<<1
        return False
