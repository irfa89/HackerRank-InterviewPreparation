"""
John works at a clothing store. He has a large pile of socks that he must pair by color for sale.
Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
"""

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sameColor = {}
    count = 0
    for key in ar:
        if key in sameColor:
            sameColor[key] += 1
        else:
            sameColor[key] = 1
    for key in sameColor:
        count += sameColor[key] // 2
    return count


if __name__ == '__main__':

    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)
