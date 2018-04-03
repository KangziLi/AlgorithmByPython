# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 00:28:04 2017

@author: KangziLi
@source: lintcode - 157. Unique Characters
"""

class Solution:
    """
    @param: str: A string
    @return: a boolean
    """
    def isUnique(self, str):
        dic ={}
        for s in str:
            if s in dic:
                return False
            else:
                dic[s]=0
        return True
        
