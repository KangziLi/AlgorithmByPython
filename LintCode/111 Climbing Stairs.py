# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 17:17:50 2017

@author: KangziLi
@source: lintcode - 111. Climbing Stairs
"""

class Solution:
    """
    You are climbing a stair case. It takes n steps to reach to the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        #if n == 1 or n==0:
        #    return 1
        #return self.climbStairs(n-1)+self.climbStairs(n-2)
        f=[0,1,2]
        for i in range(3,n+1):
            f[i%3] = f[(i-2)%3]+f[(i-1)%3]
        return f[n%3]