#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:30:03 2018

@author: Kangzi Li

LeetCode: 832. Flipping an Image
"""

# Given a binary matrix A, we want to flip the image horizontally, then invert 
# it, and return the resulting image.
# To flip an image horizontally means that each row of the image is reversed.  
# For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced 
# by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

# 1 <= A.length = A[0].length <= 20
# 0 <= A[i][j] <= 1
# Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

class Solution(object):
    

    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        mid = int(len(A) / 2) 
        
        for i in A:
            
            if len(i) % 2 == 1:
                if i[mid] == 0:
                    i[mid] = 1
                else:
                    i[mid] = 0
 
            if len(i) < 2:
                break 
                  
            for j in range(mid):
                if i[j] == i[-j-1] and i[j] == 0:
                    i[j] = 1
                    i[-j-1] = 1
                elif i[j] == i[-j-1] and i[j] == 1:
                    i[j] = 0
                    i[-j-1] = 0
        return A

    def flipAndInvertImageOpt(self, A):
        for row in A:
            # i = 0, ~i = -1 取反
            # i = 0, i^1 = 1 异或
            for i in range((len(row) + 1) / 2):
                row[i], row[~i] = row[~i]^1, row[i]^1
        return A
        
            
            
            
            
            
            
            
        