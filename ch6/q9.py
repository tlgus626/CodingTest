# BFS : 큐 구조로 구현 (first in first out)
# FIFO : 들어간 순서대로 탐색하니까, 레벨 별로 탐색이 가능함!

# 최단 거리 탐색은 무조건 BFS!!
# 1번만에 갈 수 있는 방법 모두 탐색 -> .. -> 5번만에 갈 수 있는 방법 모두 탐색

import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
A = [list(map(int, input().split())) for _ in range(7)]

check = [[0] * 7 for _ in range(7)] # 스텝 개수 세기
dQ = deque()

# initialize
A[0][0] = 1  # 한번 방문하면 벽이 되도록 설정해서 두 번 방문하지 않도록 함
dQ.append((0, 0))

while dQ:
    tmp = dQ.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        # 방문 가능 조건
        if 0 <= x <= 6 and 0 <= y <= 6 and A[x][y] == 0:
            A[x][y] = 1
            # tmp에서 (x,y)로 한번 스텝
            check[x][y] = check[tmp[0]][tmp[1]] + 1
            dQ.append((x, y))

if check[6][6] == 0 :
    print(-1)
else :
    print(check[6][6])