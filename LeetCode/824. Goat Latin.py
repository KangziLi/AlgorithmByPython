#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 18:55:27 2018

@author: Kangzi Li

LeetCode: 824. Goat Latin
"""

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = ["a","e","i","o","u"]
        ans = S.split()
        for i in range(len(ans)):
            if ans[i][0].lower() not in vowel:
                ans[i]=ans[i][1:]+ans[i][0]
            ans[i] += "ma"+"a"*(i+1)
        return ' '.join(ans)
