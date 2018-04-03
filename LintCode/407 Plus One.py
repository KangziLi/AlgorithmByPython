# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:53:52 2017

@author: KangziLi
@source: lintcode - 407. Plus One
"""

class Solution:
    """
    Given a non-negative number represented as an array of digits, plus one to the number.
    The digits are stored such that the most significant digit is at the head of the list.
    @param: digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        if len(digits)==0:
            return digits
        carry = 0
        digits[-1]+=1
        for i in range(len(digits)-1,-1,-1):
            tempcarry = (digits[i]+carry)/10
            digits[i] = (digits[i]+carry)%10
            carry = tempcarry
        if carry >0:
            digits.insert(0,1)
        return digits

