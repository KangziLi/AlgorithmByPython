"""
Created on Sun Nov 26 23:39:00 2017

@author: KangziLi
@source: lintcode - 2. Trailing Zeros
"""

class Solution:
    """
    Write an algorithm which computes the number of trailing zeros in n factorial.
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        count = 0
        while n:
            n /= 5
            count += n
        return count