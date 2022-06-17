import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())

dis = [[0] * N for _ in range(N)]
degree = [0] * N  # 각 일의 진입 차수
for i in range(N):
    dis[i][i] = 0
for _ in range(M):
    x, y = map(int, input().split())
    degree[y - 1] += 1
    dis[x - 1][y - 1] = 1

# degree == 0인 일은 선행할 작업이 없는 것
Q = deque()
for i in range(N):
    if degree[i] == 0:
        Q.append(i)

# 특정 작업을 하고 나면, 그것이 선행 작업인 작업의 진입 차수를 1 줄이기
while Q:
    # x 작업 수행
    x = Q.popleft()
    print(x + 1, end=' ')
    # x가 선행 작업인 작업의 진입 차수를 1 줄이기
    for i in range(N):
        if dis[x][i] == 1:
            degree[i] -= 1
            if degree[i] == 0:
                Q.append(i)
