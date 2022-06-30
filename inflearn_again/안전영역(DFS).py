N = 5
A = [[6, 8, 2, 6, 2], [3, 2, 3, 4, 6], [6, 7, 3, 3, 2], [7, 2, 5, 3, 6], [8, 9, 5, 2, 7]]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = 0


def DFS(X, Y, h):
    check[X][Y] = 1
    for i in range(4):
        newX = X + dx[i]
        newY = Y + dy[i]
        if 0 <= newX < N and 0 <= newY < N and check[newX][newY] == 0 and A[newX][newY] > h:
            DFS(newX, newY, h)


for h in range(100):
    check = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if check[i][j] == 0 and A[i][j] > h:
                cnt += 1
                DFS(i, j, h)
    res = max(res, cnt)
    if cnt == 0:
        break

print(res)
