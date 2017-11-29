"""
Created on Sun Nov 26 19:35:06 2017

@author: KangziLi
@source: lintcode - 365. Count 1 in Binary
"""

class Solution:
    """
    Count how many 1 in binary representation of a 32-bit integer.
    @param: num: An integer
    @return: An integer
    """
    def countOnes(self, num):
        count = 0
        for i in range(32):
            count += num & 1
            num >>= 1
        return count