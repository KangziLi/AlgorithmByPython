# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:10:11 2017

@author: KangziLi
@source: lintcode - 115. Unique Paths II
"""

class Solution:
    """
    @param: obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        oc = obstacleGrid
        for i in range(len(oc)):
            for j in range(len(oc[0])):
                if i ==0 and j ==0:
                    oc[i][j] = 1 - oc[i][j]
                elif i==0:
                    if oc[i][j] == 1:
                        oc[i][j] =0
                    else:
                        oc[i][j]=oc[i][j-1]
                elif j==0:
                    if oc[i][j] ==1:
                        oc[i][j]=0
                    else:
                        oc[i][j] = oc[i-1][j]
                else:
                    if oc[i][j] ==1:
                        oc[i][j]=0
                    else:
                        oc[i][j]=oc[i-1][j]+oc[i][j-1]
        return oc[-1][-1]
        
        
        
        
