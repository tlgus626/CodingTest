# BFS : 큐 구조로 구현 (first in first out)
# FIFO : 들어간 순서대로 탐색하니까, 레벨 별로 탐색이 가능함!

import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

cnt = 0 # 섬의 개수
dQ = deque()

for i in range(N) :
    for j in range(N) :
        # 섬 발견했으니 BFS 시작!
        if A[i][j] == 1 :
            A[i][j] = 0
            dQ.append((i, j))
            while dQ :
                tmp = dQ.popleft()
                for k in range(8) :
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0<=x<N and 0<=y<N and A[x][y] == 1 :
                        A[x][y] = 0
                        dQ.append((x, y))
            # while dQ = False 이면 섬 하나를 발견한거니까 카운트!
            cnt += 1

print(cnt)