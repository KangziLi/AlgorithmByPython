# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:23:58 2017

@author: KangziLi
@source: lintcode - 197. Permutation Index
"""

class Solution:
    """
    @param: A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        index = 1
        for i in range(len(A)):
            count = 0
            factor = 1
            for j in range(i+1,len(A)):
                if A[j] < A[i]:
                    count += 1
            if count > 0:
                for k in range(1,len(A)-i):
                    factor *= k
            index = (factor * count) + index
        return index
