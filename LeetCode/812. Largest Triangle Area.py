#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:06:36 2018

@author: Kangzi Li

LeetCode: 812. Largest Triangle Area
"""

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        # area = 0.5 * a * b * sin(c)
        # area = 0.5((x2y3-x3y2)-(x1y3-x3y1)+(x1y2-x2y1))
        def area(a, b, c):
            return 0.5 * abs(a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - a[1] * b[0] - b[1] * c[0] - a[0] * c[1])
        maxare = 0
        num = len(points)
        for i in range(num-2):
            for j in range(i+1,num-1):
                for k in range(j+1,num):
                    maxare=max(maxare,area(points[i],points[j],points[k]))
        return maxare

