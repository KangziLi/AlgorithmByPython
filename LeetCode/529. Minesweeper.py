#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 07:39:06 2018

@author: Kangzi Li

LeetCode: 529. Minesweeper
"""

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board:
            return 
        row, col = len(board), len(board[0])
        queue = []
        queue.append((click[0],click[1]))
        valis_neighbours = lambda (i, j): 0<=i<row and 0<=j<col
        while queue:
            x, y = queue.pop()
            if board[x][y] == 'M':
                board[x][y]= 'X'
            else:
                neighbours = filter(valis_neighbours, 
                                    [(x-1, y), (x+1, y), (x, y-1), (x, y+1), 
                                     (x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)])
                minecount = sum(board[i][j]=='M' for i,j in neighbours)
                if minecount >0:
                    board[x][y] = str(minecount)
                else:
                    board[x][y] = 'B'
                    queue.extend([(i,j) for (i,j) in neighbours if board[i][j]=='E'])
        return board