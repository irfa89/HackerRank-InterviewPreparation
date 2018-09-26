"""
Given an array a of n integers and a number, d , perform d left rotations on the array.
Return the updated array to be printed as a single line of space-separated integers.
"""

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
   shift = a[d:] + a[:d]
   return shift

if __name__ == '__main__':

    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)
    print(result)