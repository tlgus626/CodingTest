from collections import deque

N, M = 6, 6
I = [(1, 4), (5, 4), (4, 3), (2, 5), (2, 3), (6, 2)]

A = [[0] * N for _ in range(N)]
degree = [0] * N  # in-degree
for x, y in I:
    A[x - 1][y - 1] = 1
    degree[y - 1] += 1

Q = deque()
for i in range(N):
    if degree[i] == 0:
        Q.append(i)

while Q:
    x = Q.popleft()
    print(x + 1, end=' ')
    for i in range(N):
        if A[x][i] == 1:
            degree[i] -= 1
            if degree[i] == 0:
                Q.append(i)