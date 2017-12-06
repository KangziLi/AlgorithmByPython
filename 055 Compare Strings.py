# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 00:09:45 2017

@author: KangziLi
@source: lintcode - 55. Compare Strings
"""

class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        if len(B) == 0:
            return True
        if len(A) == 0:
            return False
        tracktable = [0] *26
        for i in A:
            tracktable[ord(i)-65]+=1
        for i in B:
            if tracktable[ord(i)-65] == 0:
                return False
            else:
                tracktable[ord(i)-65] -= 1
        return True