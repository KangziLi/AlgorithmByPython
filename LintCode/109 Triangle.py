# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 16:57:23 2017

@author: KangziLi
@source: lintcode - 109. Triangle
"""

class Solution:
    """
    Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
    @param: triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        res = [triangle[0]]
        m = len(triangle)
        for i in range(1,m):
            res.append([])
            n = len(triangle[i])
            for j in range(n):
                if j>0 and j<(len(triangle[i-1])):
                    res[i].append(min(res[i-1][j-1],res[i-1][j])+triangle[i][j])
                elif j>0:
                    res[i].append(res[i-1][j-1]+triangle[i][j])
                else:
                    res[i].append(res[i-1][j]+triangle[i][j])
        return min(res[-1])