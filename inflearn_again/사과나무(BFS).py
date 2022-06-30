from collections import deque

N = 5
A = [[10, 13, 10, 12, 15], [12, 39, 30, 23, 11], [11, 25, 50, 53, 15], [19, 27, 29, 37, 27], [19, 13, 30, 13, 19]]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
check = [[0] * N for _ in range(N)]
cnt = 0
Q = deque()

# initialize : from center
check[N // 2][N // 2] = 1
cnt += A[N // 2][N // 2]
Q.append((N // 2, N // 2))

L = 0
while True:
    if L == N // 2:
        break
    size = len(Q)
    for i in range(size):
        tmp = Q.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if check[x][y] == 0:
                cnt += A[x][y]
                check[x][y] = 1
                Q.append((x, y))
    L += 1

print(cnt)
