#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:53:11 2018

@author: Kangzi Li

LeetCode: 647. Palindromic Substrings
"""

# Given a string, your task is to count how many palindromic substrings in this 
# string.
# The substrings with different start indexes or end indexes are counted as 
# different substrings even they consist of same characters.
#
# Input: "aaa"
# Output: 6

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for c in range(2 * len(s) - 1):
            left = int(c / 2)
            right = left + c % 2
            while left >= 0 and right <len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res