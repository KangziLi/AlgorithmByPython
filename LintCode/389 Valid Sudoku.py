# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 22:51:16 2017

@author: KangziLi
@source: lintcode - 389. Valid Sudoku
"""

class Solution:
    """
    @param: board: the board
    @return: whether the Sudoku is valid
    """
    def isValidSudoku(self, board):
        row = [set([]) for i in range(9)]
        col = [set([]) for i in range(9)]
        grid = [set([]) for i in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row[r]:
                    return False
                if board[r][c] in col[c]:
                    return False
                g = r/3*3 +c/3
                if board[r][c] in grid[g]:
                    return False
                grid[g].add(board[r][c])
                row[r].add(board[r][c])
                col[c].add(board[r][c])
        return True
        