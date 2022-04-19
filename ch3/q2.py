import sys
sys.stdin = open('input.txt','rt')

K, N = map(int, input().split())

A = [int(input()) for _ in range(K)]

len = 2

while True :
    cnt = 0
    for a in A :
        cnt += a//len
    if cnt >= N :
        len += 1
    else :
        print(len-1)
        break