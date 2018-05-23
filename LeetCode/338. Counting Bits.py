#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 12:32:42 2018

@author: Kangzi Li

LeetCode: 338. Counting Bits
"""


# Given a non negative integer number num. For every numbers i in the range 
# 0 ≤ i ≤ num calculate the number of 1's in their binary representation and 
# return them as an array.
#
# Example:
# For num = 5 you should return [0,1,1,2,1,2].
#
#
# It is very easy to come up with a solution with run time O(n*sizeof(integer)). 
# But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function 
# like __builtin_popcount in c++ or in any other language.

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(1,num + 1):
            if i & 1:
                res.append(res[i>>1] + 1)
            else:
                res.append(res[i>>1])
        return res
        