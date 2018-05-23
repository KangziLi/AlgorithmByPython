#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 16:12:33 2018

@author: Kangzi Li

LeetCode: 646. Maximum Length of Pair Chain
"""

#You are given n pairs of numbers. In every pair, the first number is always 
#smaller than the second number.
#
#Now, we define a pair (c, d) can follow another pair (a, b) if and only if 
#b < c. Chain of pairs can be formed in this fashion.
#
#Given a set of pairs, find the length longest chain which can be formed. You 
#needn't use up all the given pairs. You can select pairs in any order.
#
#Input: [[1,2], [2,3], [3,4]]
#Output: 2
#Explanation: The longest chain is [1,2] -> [3,4]

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        
#       out of time
#        pairs.sort()
#        dp = [1]*len(pairs)
#        for i in range(len(pairs)):
#            for j in range(i):
#                if pairs[i][0]>pairs[j][1]:
#                    dp[i]= max(dp[i],dp[j]+1)
#        return max(dp)
        
        res, cur = 0, float('-inf')
        for p in sorted(pairs, key=lambda x: x[1]):
            if cur < p[0]: 
                cur, res = p[1], res + 1
        return res