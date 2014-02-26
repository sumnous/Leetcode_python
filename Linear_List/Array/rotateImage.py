#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-01-25
@author: Ting Wang
'''

#You are given an n x n 2D matrix representing an image.
#Rotate the image by 90 degrees (clockwise).
#Follow up:
#Could you do this in-place?

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, M):
        n = len(M)
        if n <= 1:
            return M
        if n % 2 == 0:
            for i in range(n/2):
                for j in range(n/2):
                    tmp = M[j][n-i-1]
                    M[j][n-i-1] = M[i][j]
                    M[i][j] = M[n-j-1][i]
                    M[n-j-1][i] = M[n-i-1][n-j-1]
                    M[n-i-1][n-j-1] = tmp
        else:
            for i in range(n/2):
                for j in range(n/2+1):
                    tmp = M[j][n-i-1]
                    M[j][n-i-1] = M[i][j]
                    M[i][j] = M[n-j-1][i]
                    M[n-j-1][i] = M[n-i-1][n-j-1]
                    M[n-i-1][n-j-1] = tmp
        return M

if __name__ == '__main__':
    #M = [[2,0,2],
    #     [1,0,1],
    #     [0,5,10]
    #    ]
    M = [[1,2],[3,4]]
    s = Solution()
    print s.rotate(M)
