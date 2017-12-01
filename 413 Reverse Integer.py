# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:25:37 2017

@author: KangziLi
@source: lintcode - 413. Reverse Integer
"""

class Solution:
    """
    Reverse digits of an integer. Returns 0 when the reversed integer overflows (signed 32-bit integer).
    @param: n: the integer to be reversed
    @return: the reversed integer
    """
    def reverseInteger(self, n):
        if n<10 and n>-10:
            return n
        neg = 1
        if n < 0:
            neg =-1
            n = -n
        reverse = 0
        while n>0:
            reverse = reverse * 10 + n%10
            n = n/10
        if reverse >(1<<31)-1:
            return 0
        return reverse * neg
            