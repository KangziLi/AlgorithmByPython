# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 23:53:22 2017

@author: KangziLi
@source: lintcode - 156. Merge Intervals
"""

class Solution:
    """
    @param: intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals
        intervals = sorted(intervals, key=lambda interval:interval[0])
        result = [intervals[0]]
        for i in range(1,len(intervals)):
            interval = intervals[i]
            if result[-1][-1] < interval[0]:
                result.append(interval)
            else:
                result[-1][-1] = max(result[-1][-1],interval[-1])
        return result
    
