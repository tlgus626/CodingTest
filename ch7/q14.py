import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
F = [[100]*N for _ in range(N)]
for i in range(N) :
    F[i][i] = 0
while True :
    a, b = map(int, input().split())
    if a == -1 :
        break
    else :
        F[a-1][b-1] = 1
        F[b-1][a-1] = 1

# dynamic programming
for i in range(N):
    for j in range(N):
        for k in range(N):
            F[i][j] = min(F[i][j], F[i][k] + F[k][j])

# print result
res = [0]*N
score = 100
for i in range(N) :
    for j in range(N) :
        res[i] = max(res[i], F[i][j])
    score = min(score, res[i])

out = []
for i in range(N) :
    if res[i] == score :
        out.append(i+1)

print('%d %d' %(score, len(out)))
for o in out :
    print(o, end=' ')