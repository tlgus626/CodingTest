import sys
sys.stdin = open('input.txt','rt')

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

apple = 0
center = N//2

for i in range(center) :
    for a in A[i][(center-i):(center+i+1)] :
        apple += a
    for a in A[N-1-i][(center-i):(center+i+1)] :
        apple += a

for a in A[center] :
    apple += a

print(apple)