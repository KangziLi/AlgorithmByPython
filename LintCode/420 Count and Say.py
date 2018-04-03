# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 18:53:34 2017

@author: KangziLi
@source: lintcode - 420. Count and Say
"""

class Solution:
    """
    @param: n: the nth
    @return: the nth sequence
    """
    def count(self,s):
        t=''; count=0; curr='#'
        for i in s:
            if i!=curr:
                if curr!='#':
                    t+=str(count)+curr
                curr=i
                count=1
            else:
                count+=1
        t+=str(count)+curr
        return t
    def countAndSay(self, n):
        s='1'
        for i in range(2,n+1):
            s=self.count(s)
        return s