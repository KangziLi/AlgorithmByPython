#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 13:42:34 2018

@author: Kangzi Li

LeetCode: 771. Jewels and Stones
"""


#You're given strings J representing the types of stones that are jewels, and S 
#representing the stones you have.  Each character in S is a type of stone you 
#have.  You want to know how many of the stones you have are also jewels.
#
#The letters in J are guaranteed distinct, and all characters in J and S are 
#letters. Letters are case sensitive, so "a" is considered a different type of 
#stone from "A".
#
#Example 1:
#
#Input: J = "aA", S = "aAAbbbb"
#Output: 3
#Example 2:
#
#Input: J = "z", S = "ZZ"
#Output: 0
#Note:
#
#S and J will consist of letters and have length at most 50.
#The characters in J are distinct.


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        Jewels = set(J)
        ans = 0
        for i in range(len(S)):
            if S[i] in Jewels:
                ans += 1
        return ans
        
        









