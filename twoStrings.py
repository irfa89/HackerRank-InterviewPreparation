import sys

def twoStrings(s1,s2):
    l1 = list(s1)
    l2 = list(s2)
    if bool(set(l1).intersection(l2)):
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s1 = input()
        s2 = input()
        result = twoStrings(s1, s2)
        print(result)
