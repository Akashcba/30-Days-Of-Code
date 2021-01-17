# Day 10
# Binary Numbers
# Return the maximum count of consecutive 1's
# in the binary representation of the number

## Use n&1: to check if its odd or not
## Use n>>1 to divide by 2 once

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    max_m = 0 ;temp = 0
    while(n):
        if n&1:
            temp += 1
            if max_m < temp:
                max_m = temp
        else :
            temp = 0
        n = n>>1
    print(max_m)
