# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:33:52 2017

@author: KangziLi
@source: lintcode - 200. Longest Palindromic Substring
"""

class Solution:
    """
    Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
    @param: s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        tempstr = '#' + '#'.join(s)+'#'
        lens = len(tempstr)
        RL = [0]* lens
        maxright = 0
        pos = 0
        maxlenpos = 0
        for i in range(lens):
            if i < maxright:
                RL[i] = min(maxright-i, RL[2*pos-i])
            else:
                RL[i] = 1
            while i-RL[i]>=0 and i+RL[i]<lens and tempstr[i-RL[i]]==tempstr[i+RL[i]]:
                RL[i]+=1
            if (i-1+RL[i])>maxright:
                maxright = RL[i] + i -1
                pos = i
            if RL[maxlenpos]<RL[i]:
                maxlenpos = i
        resstr=""
        for x in range(maxlenpos-RL[maxlenpos]+2,maxlenpos+RL[maxlenpos]-1,2):
                resstr = resstr+tempstr[x]
        return resstr
        