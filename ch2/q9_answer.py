import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

A.insert(0, [0]*(N+2))
A.append([0]*(N+2))
for a in A :
    a.insert(0, 0)
    a.append(0)

cnt = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(1, N+1) :
    for j in range(1, N+1) :
        if all(A[i][j]>A[i+dx[k]][j+dy[k]] for k in range(4)) :
            cnt += 1

print(cnt)