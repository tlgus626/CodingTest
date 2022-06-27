import sys

N = 6
S = [1, 3, 5, 6, 7, 10]
check = [0] * N
TOTAL = sum(S)


def DFS(v):
    if v == N:
        SUM = 0
        for i in range(N):
            if check[i] == 1:
                SUM += S[i]
        # early stopping
        if SUM > TOTAL // 2:
            return
        if SUM == TOTAL - SUM:
            print('YES')
            sys.exit(0)
    else:
        check[v] = 1
        DFS(v + 1)
        check[v] = 0
        DFS(v + 1)


DFS(0)
print('NO')
