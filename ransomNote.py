""""
Complete the checkMagazine function in the editor below. It must print YES if the note can be formed using the magazine, or No.

checkMagazine has the following parameters:
magazine: an array of strings, each a word in the magazine
note: an array of strings, each a word in the ransom note.
"""


import math
import os
import random
import re
import sys

# Complete the checkMagazine function below. - Did not pass all 22 test cases.
""" 
def checkMagazine(magazine, note):
    mag = list(magazine)
    for r in note:
        if r in mag:
            mag.remove(r)
        else:
            return False
    return True
"""
# Passed all test cases - code inspired from leetcode.
def checkMagazine(magazine, note):
    d = dict()
    for char in magazine:
        d[char] = d.get(char, 0) + 1
    for char in note:
        if(char not in d or d[char] <= 0):
            return False
        d[char] = d.get(char, 0) - 1
    return True

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
    if checkMagazine(magazine, note) == True:
        print("Yes")
    else:
        print("No")