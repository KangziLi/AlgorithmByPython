# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:43:26 2017

@author: KangziLi
@source: lintcode - 13. strStr
"""

class Solution:
    """
    For a given source string and a target string, you should output the first index(from 0) of target string in source string.
    If target does not exist in source, just return -1.
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """
    def strStr(self, source, target):
        if source is None or target is None:
            return -1
        return source.find(target)