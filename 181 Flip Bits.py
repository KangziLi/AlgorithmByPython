# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 13:45:29 2017

@author: KangziLi
@source: lintcode - 181. Flip Bits
"""

class Solution:
    """
    @param: a: An integer
    @param: b: An integer
    @return: An integer
    """
    def bitSwapRequired(self, a, b):
        k = a ^ b
        cnt = 0
        for i in range(32):
            if k & (1<<i) != 0:
                cnt+=1
        return cnt