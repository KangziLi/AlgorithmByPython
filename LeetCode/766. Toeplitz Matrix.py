#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:33:14 2018

@author: Kangzi Li

LeetCode: 766. Toeplitz Matrix
"""

# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
#
# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
#
# matrix will be a 2D array of integers.
# matrix will have a number of rows and columns in range [1, 20].
# matrix[i][j] will be integers in range [0, 99].
#
# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: True

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(0,len(matrix)-1):
            if matrix[i][:-1] != matrix[i+1][1:]: 
                return False
        return True
        