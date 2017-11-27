"""
Created on Mon Nov 27 18:05:40 2017

@author: 18316
@source: lintcode - 3. Digit Counts
"""

class Solution:
    """
    Count the number of k's between 0 and n. k can be 0 - 9.
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCounts(self, k, n):
        assert(n >= 0 and 0 <= k <= 9)
        count = 0
        base = 1
        while n / base > 0:
            curbit = (n / base) % 10
            lowbit = n - (n / base) * base
            highbit = n /(base * 10)
            if curbit < k:
                count += highbit * base
            elif curbit == k:
                count += highbit * base + lowbit + 1
            else:
                count += (highbit +1) * base
            base *= 10
        if k == 0:
            if n == 0:
                count = 1
            else:
                count -= base / 10 
        return count