# BFS : 큐 구조로 구현 (first in first out)
# FIFO : 들어간 순서대로 탐색하니까, 레벨 별로 탐색이 가능함!

# 중심 cell부터 상하좌우 탐색을 level 별로 하면, 마름모꼴이 되겠지!

import sys
from collections import deque

sys.stdin = open('input.txt','r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

check = [[0]*N for _ in range(N)]
cnt = 0
dQ = deque()

# initialize : 중심 cell부터 시작해서 상하좌우 탐색
check[N//2][N//2] = 1
cnt += A[N//2][N//2]
dQ.append((N//2, N//2))

L = 0
while True :
    if L == N//2 :
        break
    size = len(dQ) # 처음엔 1이겠지
    # size만큼 반복문이 돌면서 BFS 가능해짐
    for i in range(size) :
        tmp = dQ.popleft()
        for j in range(4) :
            x = tmp[0]+dx[j]
            y = tmp[1]+dy[j]
            if check[x][y] == 0 :
                cnt += A[x][y]
                check[x][y] = 1
                dQ.append((x, y))
    L += 1

print(cnt)