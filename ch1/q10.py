import sys
sys.stdin = open('input.txt','rt')

N = int(input())
Qs = list(map(int, input().split()))

score = [0]*N

if Qs[0] == 1 :
    score[0] = 1

for i in range(1,N) :
    if Qs[i] == 1 :
        score[i] += 1
    if Qs[i] == Qs[i-1] :
        score[i] += score[i-1]

print(sum(score))