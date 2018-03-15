# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 13:45:24 2017

@author: KangziLi
@source: lintcode - 185. Matrix Zigzag Traversal
"""

class Solution:
    """
    @param: matrix: An array of integers
    @return: An array of integers
    """
    def printZMatrix(self, matrix):
        if len(matrix) ==0:
            return []
        x,y = 0,0
        m,n = len(matrix),len(matrix[0])
        row,col = range(m),range(n)
        result = []
        dx = [1,-1]
        dy = [-1,1]
        direct = 1
        for i in range(m*n):
            result.append(matrix[x][y])
            nextx = x + dx[direct]
            nexty = y + dy[direct]
            if nextx not in row or nexty not in col:
                if direct ==1:
                    if nexty >= n:
                        nextx,nexty = x+1,y
                    else:
                        nextx,nexty = x,y+1
                else:
                    if nextx >= m:
                        nextx,nexty = x,y+1
                    else:
                        nextx,nexty = x+1,y
                direct = 1-direct
            x,y =nextx,nexty
        return result



