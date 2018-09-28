"""
Complete the makeAnagram function in the editor below. It must return an integer representing the minimum total characters
that must be deleted to make the strings anagrams.
makeAnagram has the following parameter(s):
a: a string
b: a string
"""

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    cnt = [0] * 26
    offset = ord('a')
    for char in a:
        cnt[ord(char) - offset] += 1
    for char in b:
        cnt[ord(char) - offset] -= 1
    total = 0
    for value in cnt:
        total += abs(value)
    return total

if __name__ == '__main__':
    a = input()
    b = input()
    res = makeAnagram(a, b)
    print(res)

