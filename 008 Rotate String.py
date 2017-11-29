# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 08:46:58 2017

@author: KangziLi
@source: lintcode - 8. Rotate String
"""

class Solution:
    """
    Given a string and an offset, rotate string by offset. (rotate from left to right)
    @param: str: An array of char
    @param: offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        if not offset: return
        if not str: return
        n = len(str)
        offset = offset%n
        for i in range(offset):
            t = str.pop()
            str.insert(0,t) 