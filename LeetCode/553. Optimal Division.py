#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:50:00 2018

@author: Kangzi Li

LeetCode: 553. Optimal Division
"""

class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        ans = list(map(str,nums))
        if len(ans) <= 2:
            return '/'.join(ans)
        return ans[0]+'/('+'/'.join(ans[1:])+')'
