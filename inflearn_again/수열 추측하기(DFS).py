import sys

N, F = 4, 16
P = [0] * N
B = [1] * N
for i in range(1, N - 1):
    B[i] = (B[i - 1] * (N - i)) / i
check = [0] * (N + 1)


def DFS(L, S):
    if L == N and S == F:
        for p in P:
            print(p, end=' ')
        sys.exit()
    else:
        for i in range(1, N + 1):
            if check[i] == 0:
                check[i] = 1
                P[L] = i
                DFS(L + 1, S + P[L] * B[L])
                check[i] = 0


DFS(0, 0)
