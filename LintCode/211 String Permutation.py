# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:24:16 2017

@author: KangziLi
@source: lintcode - 211. String Permutation
"""

class Solution:
    """
    @param: A: a string
    @param: B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):
        if len(A) != len(B):
            return False
        dic = {}
        for a in A:
            if a in dic:
                dic[a] += 1
            else:
                dic[a] = 1
        for b in B:
            if b in dic and dic[b] > 0:
                dic[b] -= 1
            else:
                return False
        return True