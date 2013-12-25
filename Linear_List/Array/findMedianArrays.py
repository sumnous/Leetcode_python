#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-12-25
@author: Ting Wang
'''

# There are two sorted arrays A and B of size m and n respectively.
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log(m + n)).

def findMedianSortedArrays(A, m, B, n):
    total = m + n
    if total & 0x1:
        return find_kth(A, m, B, n, (total/2+1))
    else:
        return float(float(find_kth(A, m, B, n, total/2)+find_kth(A, m, B, n, total/2+1))/2)

def find_kth(A, m, B, n, k):
    # always assume that m is equal or smaller than n
    if m > n:
        return find_kth(B, n, A, m, k)
    if m == 0:
        return B[k-1]
    if k == 1:
        return min(A[0], B[0])
    # divide k into two parts
    pa = min(k/2, m)
    pb = k - pa
    if A[pa-1] < B[pb-1]:
        return find_kth(A[pa:], m-pa, B, n, k-pa)
    elif A[pa-1] > B[pb-1]:
        return find_kth(A, m, B[pb:], n-pb, k-pb)
    elif A[pa-1] == B[pb-1]:
        return A[pa-1]

if __name__ == '__main__':
    A = [2,4,6]
    B = [1,3,5,7,9]
    m = len(A)
    n = len(B)
    print findMedianSortedArrays(A, m, B, n)





