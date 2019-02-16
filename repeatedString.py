import sys

""" # Overflow error 
def repeatedString(s):
    return s.count('a')

def repeatToLength(s,l):
    if l > 0 :
        a = (s*(l//len(s)+1))[:l]
        return a
    else:
        return s
"""


if __name__ == '__main__':

    s = input()
    n = int(input())
    print(s.count('a')*(n//len(s)+s[:n% len(s)].count('a')))
