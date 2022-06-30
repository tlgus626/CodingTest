from collections import deque

A = [[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 0, 0, 0],
     [1, 1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0, 0]]
check = [[0] * 7 for _ in range(7)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
Q = deque()

# initialize
Q.append((0, 0))
A[0][0] = 1

while Q:
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0 <= x <= 6 and 0 <= y <= 6 and A[x][y] == 0:
            A[x][y] = 1
            check[x][y] = check[tmp[0]][tmp[1]] + 1
            Q.append((x, y))

if check[6][6] == 0:
    print(-1)
else:
    print(check[6][6])
