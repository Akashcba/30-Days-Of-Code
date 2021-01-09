# Day 2
# Working with operators ...
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    return meal_cost*(tip_percent*0.01 + tax_percent*0.01 + 1)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    print(round(solve(meal_cost, tip_percent, tax_percent)))
