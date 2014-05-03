#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-02-24
@author: Ting Wang
'''

# Leetcode: Valid Sudoku
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# A partially filled sudoku which is valid.

# board is a 9*9 2D array
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        # check row
        for row in board:
            tmp = []
            for i in row:
                if i != '.':
                    if i not in tmp:
                        tmp.append(i)
                    else:
                        return False
        # check column
        for i in xrange(9):
            tmp = []
            for j in xrange(9):
                k = board[j][i]
                if k != '.':
                    if k not in tmp:
                        tmp.append(k)
                    else:
                        return False
        # check 3*3 subboard
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                tmp = []
                for m in [0, 1, 2]:
                    for n in [0, 1, 2]:
                        k = board[i+m][j+n]
                        if k != '.':
                            if k not in tmp:
                                tmp.append(k)
                            else:
                                return False
        return True

if __name__ == '__main__':
    M = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]
    s = Solution()
    print s.isValidSudoku(M)

