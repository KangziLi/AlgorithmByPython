"""
Created on Sun Nov 26 22:54:06 2017

@author: KangziLi
@source: lintcode - 1. A + B Problem
"""

class Solution:
    """
    Write a function that add two numbers A and B. You should not use + or any arithmetic operators.
    @param: a: An integer
    @param: b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        INT_RANGE = 0xFFFFFFFF
        while b:
            a,b = a ^ b, (a & b)<<1
            a &= INT_RANGE
        if a >>31 == 0:
            return a
        else:
            return a ^ ~INT_RANGE