# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 15:42:48 2017

@author: KangziLi
@source: lintcode - 65. Median of two Sorted Arrays
"""

class Solution:
    """、
    There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        if n%2 ==1:
            return self.findKth(A,B,n/2+1)
        else:
            smaller = self.findKth(A,B, n/2)
            bigger = self.findKth(A,B,n/2+1)
            return (smaller + bigger) / 2.0
    
    def findKth(self, A,B,k):
        if len(A) ==0:
            return B[k-1]
        if len(B) == 0:
            return A[k-1]
        if k == 1:
            return min(A[0],B[0])
        if len(A) >= k/2:
            a = A[ k/2 -1] 
        else: 
            a = None
        if len(B) >= k/2:
            b = B[ k/2 -1] 
        else: 
            b = None
        if (a is not None and a<b) or b is None:
            return self.findKth(A[k / 2:], B, k - k / 2)
        return self.findKth(A, B[k / 2:], k - k / 2)






