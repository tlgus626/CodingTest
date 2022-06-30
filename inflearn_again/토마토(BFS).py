from collections import deque

M, N = 6, 4
T = [[0, 0, -1, 0, 0, 0], [0, 0, 1, 0, -1, 0], [0, 0, -1, 0, 0, 0], [0, 0, 0, 0, -1, 1]]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
days = [[0] * M for _ in range(N)]

Q = deque()

for i in range(N):
    for j in range(M):
        if T[i][j] == 1:
            Q.append((i, j))

while Q:
    tmp = Q.popleft()
    for i in range(4):
        newX = tmp[0] + dx[i]
        newY = tmp[1] + dy[i]
        if 0 <= newX < N and 0 <= newY < M and T[newX][newY] == 0:
            days[newX][newY] = days[tmp[0]][tmp[1]] + 1
            T[newX][newY] = 1
            Q.append((newX, newY))

print(T)
print(days)
