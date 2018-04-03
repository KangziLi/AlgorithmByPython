# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 19:07:07 2017

@author: KangziLi
@source: lintcode - 30. Insert Interval
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param: intervals: Sorted interval list.
    @param: newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        result = []
        inserpos = 0
        for interval in intervals:
            if interval.end< newInterval.start:
                result.append(interval)
                inserpos += 1
            elif interval.start >newInterval.end:
                result.append(interval)
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end,newInterval.end)
        result.insert(inserpos,newInterval)
        return result
