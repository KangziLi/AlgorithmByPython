# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 23:41:10 2017

@author: KangziLi
@source: lintcode - 5. Kth Largest Element
"""

class Solution:
    '''
    Find K-th largest element in an array.
    @param k & A a integer and an array
    @return ans a integer
    '''
    def kthLargestElement(self, k, A):
        A.sort()
        return A[-k]