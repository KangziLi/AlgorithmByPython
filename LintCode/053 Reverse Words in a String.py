# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:44:01 2017

@author: KangziLi
@source: lintcode - 53. Reverse Words in a String
"""

class Solution:  
    #Given an input string, reverse the string word by word.
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        return ' '.join(reversed(s.strip().split()))