"""
Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above.
Once sorted, print the following three lines:

Array is sorted in numSwaps swaps.,numSwap where  is the number of swaps that took place.
First Element: firstElement, where firstElement is the first element in the sorted array.
Last Element: lastElement, where lastElement  is the last element in the sorted array.
"""

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    l = len(a)
    numSwap = 0
    for i in range(l):
        for j in range(l-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                numSwap += 1
    print('Array is sorted in %d swaps.' % numSwap)
    print('First Element: %d' % a[0])
    print('Last Element: %d' % a[-1])

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)
