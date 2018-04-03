# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 21:52:36 2017

@author: KangziLi
@source: lintcode - 64. Merge Sorted Array
"""

class Solution:
    """
    Given two sorted integer arrays A and B, merge B into A as one sorted array.
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        res = []
        i, j =0, 0
        while i<m and j<n:
            if A[i]<B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1
        while i<m:
            res.append(A[i])
            i += 1
        while j<n:
            res.append(B[j])
            j += 1
        for k in range(m + n):
            A[k]=res[k]
