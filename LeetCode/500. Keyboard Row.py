#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 15:55:35 2018

@author: Kangzi Li

LeetCode: 500. Keyboard Row
"""

#Given a List of words, return the words that can be typed using letters of 
#alphabet on only one row's of American keyboard like the image below.
#Input: ["Hello", "Alaska", "Dad", "Peace"]
#Output: ["Alaska", "Dad"]

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = ['qwertyuiop','asdfghjkl','zxcvbnm']
        ans = []
        for w in words:
            tw = set(w.lower())
            if tw <= set(keyboard[0]) or tw <= set(keyboard[1]) or tw <= set(keyboard[2]):
                ans.append(w)
        return ans
                