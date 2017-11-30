# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:51:23 2017

@author: KangziLi
@source: lintcode - 463. Sort Integers
"""

class Solution:
    """
    @param: A: an integer array
    @return: 
    """
    def sortIntegers(self, A):
        # bubble sort method
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i] > A[j]:
                    A[i], A[j]= A[j],A[i]
        return A