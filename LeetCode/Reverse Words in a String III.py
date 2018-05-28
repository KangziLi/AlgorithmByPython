#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 18:49:17 2018

@author: Kangzi Li

LeetCode: Reverse Words in a String III
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = s.split()
        for a in range(len(ans)):
            ans[a] = ans[a][::-1]
        return ' '.join(ans)
