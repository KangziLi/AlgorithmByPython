# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 17:52:17 2017

@author: KangziLi
@source: lintcode - 384. Longest Substring Without Repeating Characters
"""

class Solution:
    """
    Given a string, find the length of the longest substring without repeating characters.
    @param: s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        strdic = {}
        flag = 0
        result = 0
        for i in range(len(s)):
            if s[i] in strdic and strdic[s[i]] >= flag:
                flag = strdic[s[i]] +1
            strdic[s[i]] = i
            result = max(result, i - flag + 1)
        return result
             
                