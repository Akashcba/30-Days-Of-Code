## Print the maximum hourglass sum
#!/bin/python3

## O(N^2)

import math
import os
import random
import re
import sys

def find_sum(ls,r,c):
    sum = ls[r+0][c+0] + ls[r+0][c+1]+ ls[r+0][c+2] + ls[r+1][c+1] + ls[r+2][c+0] + ls[r+2][c+1] + ls[r+2][c+2]
    return sum

def max_hour_glass(arr):
    max_sum = -sys.maxsize - 1    ## Minimum value possible for int object
    for row in range(0,4): ## Because hourglass is possible till 4th row index only
        for col in range(0,4):
            sum = find_sum(arr,row,col)
            max_sum = max(sum,max_sum)
    return max_sum

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(max_hour_glass(arr))
