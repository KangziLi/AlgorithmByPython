# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 00:28:16 2017

@author: KangziLi
@source: lintcode - 158. Two Strings Are Anagrams
"""

class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i]=1
        for j in t:
            if j in dic and dic[j]!=0:
                dic[j] -= 1
            else:
                return False
        return True
        