N = 7
A = [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1],
     [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0]]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = list()


def DFS(X, Y):
    global cnt
    cnt += 1
    A[X][Y] = 0
    for i in range(4):
        newX = X + dx[i]
        newY = Y + dy[i]
        if 0 <= newX < N and 0 <= newY < N and A[newX][newY] == 1:
            DFS(newX, newY)


for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            cnt = 0
            DFS(i, j)
            res.append(cnt)

print(len(res))
for r in sorted(res):
    print(r)
