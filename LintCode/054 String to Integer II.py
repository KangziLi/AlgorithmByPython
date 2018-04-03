# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 11:36:44 2017

@author: KangziLi
@source: lintcode - 54. String to Integer II
"""

class Solution:
    """
    Implement function atoi to convert a string to an integer.
    If no valid conversion could be performed, a zero value is returned.
    If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
    @param: str: A string
    @return: An integer
    """
    def atoi(self, str):
        if len(str) ==0:
            return 0
        sgn, num, p = 0, 0, 0
        imin, imax = -1<<31, (1<<31)-1
        while str[p] ==' ':
            p += 1
        if str[p] == '-' or str[p] == '+':
            sgn = 1 if str[p] == '-' else 0
            p += 1
        while p < len(str) and str[p]>='0' and str[p] <='9':
            num = num*10 + ord(str[p])-ord('0')
            x = -num if sgn else num
            if x<imin:
                return imin
            if x>imax:
                return imax
            p += 1
        return -num if sgn else num
        
        
