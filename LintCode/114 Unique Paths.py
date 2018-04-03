# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:10:07 2017

@author: KangziLi
@source: lintcode - 114. Unique Paths
"""

class Solution:
    """
    A robot is located at the top-left corner of a m x n grid.
    The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.
    How many possible unique paths are there?
    @param: m: positive integer (1 <= m <= 100)
    @param: n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        path = {}
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    path[(i,j)]=1
                else:
                    path[(i,j)] = path[(i-1,j)] + path[(i,j-1)]
        return path[(m-1,n-1)]