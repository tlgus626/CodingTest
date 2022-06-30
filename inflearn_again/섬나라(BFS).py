from collections import deque

N = 7
A = [[1, 1, 0, 0, 0, 1, 0], [0, 1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 1],
     [1, 1, 0, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 0]]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

cnt = 0
dQ = deque()

for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            A[i][j] = 0
            dQ.append((i, j))
            while dQ:
                tmp = dQ.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0 <= x < N and 0 <= y < N and A[x][y] == 1:
                        A[x][y] = 0
                        dQ.append((x, y))
            cnt += 1

print(cnt)
