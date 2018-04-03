# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 10:05:24 2017

@author: KangziLi
@source: lintcode - 22. Flatten List
"""

class Solution(object):
    # Given a list, each element in the list can be a list or integer. flatten it into a simply list with integers.
    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        if isinstance(nestedList,int):
            return [nestedList]
        result = []
        for i in nestedList:
            result.extend(self.flatten(i))
        return result