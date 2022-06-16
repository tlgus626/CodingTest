import sys

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())

# setting
cost = [[float('inf')] * N for _ in range(N)]
for i in range(N):
    cost[i][i] = 0
for i in range(M):
    x, y, c = map(int, input().split())
    cost[x - 1][y - 1] = c

# dynamic programming
for i in range(N):
    for j in range(N):
        for k in range(N):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

# print
for i in range(N):
    for j in range(N):
        if cost[i][j] == float('inf'):
            print('M', end=' ')
        else:
            print(cost[i][j], end=' ')
    print()