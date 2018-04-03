# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 17:36:57 2017

@author: KangziLi
@source: lintcode - 28. Search a 2D Matrix
"""

class Solution:
    """
    Write an efficient algorithm that searches for a value in an m x n matrix.
    This matrix has the following properties:
    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        n, m = len(matrix), len(matrix[0])
        start, end = 0, n*m-1
        while start+1<end:
            mid = (start + end)/2
            x, y = mid/m, mid%m
            if matrix[x][y] == target:
                return True
            elif matrix[x][y]<target:
                start = mid
            else:
                end = mid
        x, y = start / m, start % m
        if matrix[x][y] == target:
            return True        
        x, y = end / m, end % m
        if matrix[x][y] == target:
            return True
        return False