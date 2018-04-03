# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 18:43:18 2017

@author: KangziLi
@source: lintcode - 491. Palindrome Number
"""

class Solution:
    """
    Check a positive number is a palindrome or not.
    A palindrome number is that if you reverse the whole number you will get exactly the same number.
    @param: num: a positive number
    @return: true if it's a palindrome or false
    """
    def isPalindrome(self, num):
        n=str(num)
        m=n[::-1]
        return n==m
        