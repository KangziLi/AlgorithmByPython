#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 08:23:01 2018

@author: Kangzi Li

LeetCode: 773. Sliding Puzzle
"""

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        target = [1,2,3,4,5,0]
        state = [x for y in board for x in y]
        if state == target:
            return 0
        d = {0:[1,3], 1:[0,2,4], 2:[1,5], 3:[0,4], 4:[1,3,5], 5:[2,4]}
        arrived = {tuple(state)}
        front = [[state.index(0),None,state]]
        distance = 0
        
        while front:
            distance += 1
            nfront = []
            while front:
                idx,last,curstate = front.pop()
                for nex in d[idx]:
                    new = curstate[:]
                    new[idx], new[nex] = new[nex], new[idx]
                    if new == target:
                        return distance
                    tnew = tuple(new)
                    if tnew not in arrived:
                        nfront.append([nex,idx,new])
                        arrived.add(tnew)
            front = nfront
        return -1
