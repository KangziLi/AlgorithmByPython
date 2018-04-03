# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:05:08 2017

@author: KangziLi
@source: lintcode - 133. Longest Words
"""

class Solution:
    """
    Given a dictionary, find all of the longest words in the dictionary.
    @param: dictionary: an array of strings
    @return: an arraylist of strings
    """
    def longestWords(self, dictionary):
        maxlen = max(len(w) for w in dictionary)
        return [w for w in dictionary if len(w) == maxlen ]
