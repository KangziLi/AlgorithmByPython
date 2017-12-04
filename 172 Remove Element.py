# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 22:07:45 2017

@author: KangziLi
@source: lintcode - 172. Remove Element
"""

class Solution:
    """
    Given an array and a value, remove all occurrences of that value in place and return the new length.
    The order of elements can be changed, and the elements after the new length don't matter.
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        j = len(A)-1
        for i in range(len(A)-1,-1,-1):
            if A[i]==elem:
                A[i],A[j]=A[j],A[i]
                j-=1
        return j+1
