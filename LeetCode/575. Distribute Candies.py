#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 16:05:56 2018

@author: Kangzi Li

LeetCode: 575. Distribute Candies
"""

#Given an integer array with even length, where different numbers in this array 
#represent different kinds of candies. Each number means one candy of the 
#corresponding kind. You need to distribute these candies equally in number to 
#brother and sister. Return the maximum number of kinds of candies the sister 
#could gain.

#Input: candies = [1,1,2,3]
#Output: 2
#Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1]. 
#The sister has two different kinds of candies, the brother has only one kind of candies. 

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(candies)/2,len(set(candies)))
        









