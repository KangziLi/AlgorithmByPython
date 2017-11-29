"""
Created on Mon Nov 27 19:03:40 2017

@author: KangziLi
@source: lintcode - 4. Ugly Number II
"""

class Solution:
    """
    Ugly number is a number that only have factors 2, 3 and 5.
Design an algorithm to find the nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...
    @param: n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        list = [1]
        i2, i3, i5=0,0,0
        while len(list)<n:
            m2 = list[i2]*2
            m3 = list[i3]*3
            m5 = list[i5]*5
            m =min(m2,m3,m5)
            if m == m2:
                i2 += 1
            if m==m3:
                i3 += 1
            if m==m5:
                i5 +=1
            list.append(m)
        return list[-1]