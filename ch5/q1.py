import sys

sys.stdin = open('input.txt', 'r')

N = int(input())


def binary(n, res):
    d = n // 2
    m = n % 2
    res.append(m)
    if d > 0:
        binary(d, res)
    elif d == 0:
        while res:
            print(res.pop(), end='')


res = []
binary(N, res)
