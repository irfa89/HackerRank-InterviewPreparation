"""
Complete the countingValleys function in the editor below. It must return an integer that denotes the number of
valleys Gary traversed.

countingValleys has the following parameter(s):

n: the number of steps Gary takes
s: a string describing his path
"""

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    lvl = 0
    count = 0
    for char in s:
        if char == "U" :
            lvl += 1
        else:
             if lvl == 0:
                 count += 1
             lvl -=1
    return count

if __name__ == '__main__':

    n = int(input())
    s = input()
    result = countingValleys(n, s)
    print(result)