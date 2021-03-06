#!/bin/python

import sys
import os

# Complete the function below.


# Complete the function below.

def valid(i, j, n):
    return i >= 0 and j >= 0 and  i < n and j < n


def findThreat(i, j, n, a):
    count = 0
    found = [[False for x in range(2)] for x in range(2)]
    for ii in range(n):
        if ii == i:
            continue
        j1 = j - (i - ii)
        j2 = j + (i - ii)
        
        if not found[ii>i][j1>j] and valid(ii, j1, n):
            if j1 == a[ii]-1:
                count += 1
                found[ii>i][j1>j] = True
        if not found[ii>i][j2>j] and valid(ii, j2, n):
            if j2 == a[ii] -1:
                count += 1
                found[ii>i][j2>j] = True

    return count


def maxThreats(a):
    if not a:
        return 0
    result = 0
    for i in range(len(a)):
        result = max(result, findThreat(i, a[i]-1, len(a), a))

    return result

input = []
while True:
    s = raw_input()
    if s:
        input.append(int(s))
    else:
        break

for i in range(len(input)):
    print i, " ", input[i] -1
print maxThreats(input)
