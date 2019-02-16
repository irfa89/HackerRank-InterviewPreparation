import sys


def jumpingOnClouds(c):
    i=0
    res=0
    while i < len(c)-1:
        if c[i]+2 < len(c) and c[i]==0:
            res += 1
            i += 2
        else:
            res += 1
            i +=1
    return res

if  __name__ == '__main__':
    n = int(input())
    c = list(map(int,input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)