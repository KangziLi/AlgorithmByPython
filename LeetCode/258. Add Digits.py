#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 14:25:52 2018

@author: Kangzi Li

LeetCode: 258. Add Digits
"""
#Input: 38
#Output: 2 
#Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#             Since 2 has only one digit, return it.

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return num
        else:
            return 1+(num-1)%9
        