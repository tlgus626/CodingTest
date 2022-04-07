import sys
sys.stdin = open('input.txt','rt')

N = int(input())
Qs = list(map(int, input().split()))

score = 0
weight = 0

for i in range(N) :
    if Qs[i] == 1 :
        weight += 1
        score += weight
    else :
        weight = 0

print(score)