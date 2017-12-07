# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:59:39 2017

@author: KangziLi
@source: lintcode - 110. Minimum Path Sum
"""

class Solution:
    """
    Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right 
    @param: grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        if grid is None:
            return 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0 and i > 0:
                    grid[i][j] +=grid[i-1][j]
                elif i>0 and j>0:
                    grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        return grid[m-1][n-1]
        
        
        
        
        
        
        
        
        
        
        