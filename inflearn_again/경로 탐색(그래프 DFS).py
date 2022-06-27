N, M = 5, 9
C = [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 5), (3, 4), (4, 2), (4, 5)]
G = [[0] * N for _ in range(N)]
for c in C:
    G[c[0] - 1][c[1] - 1] = 1
cnt = 0
check = [0] * N
check[0] = 1  # when starting, visit first node


def DFS(L):
    global cnt
    if L == N - 1:
        cnt += 1
        return
    else:
        for i in range(N):
            if G[L][i] == 1 and check[i] == 0:
                check[i] = 1
                DFS(i)
                check[i] = 0


DFS(0)
print(cnt)
