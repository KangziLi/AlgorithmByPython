#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 15:42:41 2018

@author: Kangzi Li

LeetCode: 712. Minimum ASCII Delete Sum for Two Strings
"""

#Given two strings s1, s2, find the lowest ASCII sum of deleted characters to 
#make two strings equal.
#Input: s1 = "sea", s2 = "eat"
#Output: 231
#0 < s1.length, s2.length <= 1000.
#All elements of each string will have an ASCII value in [97, 122].

class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        r = len(s1)
        c = len(s2)
        dp = [[0] * (c + 1) for _ in range(r + 1)]
        
        for i in range(r-1,-1,-1):
            dp[i][c] = dp[i+1][c] + ord(s1[i])
        for i in range(c-1,-1,-1):
            dp[r][i] = dp[r][i+1] + ord(s2[i])        
        
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                if s1[i]==s2[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    dp[i][j]=min(dp[i+1][j]+ord(s1[i]),dp[i][j+1]+ord(s2[j]))
        return dp[0][0]
                    