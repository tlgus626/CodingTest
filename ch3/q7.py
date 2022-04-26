import sys
sys.stdin = open('input.txt','r')

L = int(input())
A = list(map(int, input().split()))
M = int(input())

A.sort()

for _ in range(M) :
    A[L-1] -= 1
    A[0] += 1
    A.sort()

print(A[L-1]-A[0])