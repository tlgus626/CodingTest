# BFS : 큐 구조로 구현 (first in first out)
# FIFO : 들어간 순서대로 탐색하니까, 레벨 별로 탐색이 가능함!

import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

M, N = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
days = [[0]*M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

Q = deque()

# 익은 토마토들을 각 출발점으로 삼기
for i in range(N) :
    for j in range(M) :
        if T[i][j] == 1 :
            Q.append((i,j))

while Q :
    tmp = Q.popleft()
    for i in range(4) :
        newX = tmp[0] + dx[i]
        newY = tmp[1] + dy[i]
        if 0<=newX<N and 0<=newY<M and T[newX][newY] == 0 :
            days[newX][newY] = days[tmp[0]][tmp[1]] + 1
            T[newX][newY] = 1
            Q.append((newX, newY))

# 안익은 토마토가 있으면 -1 출력
CANT = 1
for i in range(N) :
    for j in range(M) :
        if T[i][j] == 0 :
            CANT = 0

# 안익은 토마토가 없으면 익은 일수 출력
MAX = 0
if CANT == 1 :
    for i in range(N) :
        for j in range(M) :
            if days[i][j] > MAX :
                MAX = days[i][j]
    print(MAX)
else :
    print(-1)