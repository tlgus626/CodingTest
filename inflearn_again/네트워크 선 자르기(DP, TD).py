N = 7
dy = [0] * (N + 1)


def DFS(L):
    # memoization
    if dy[L] > 0:
        return dy[L]
    if L == 1 or L == 2:
        return L
    else:
        dy[L] = DFS(L - 1) + DFS(L - 2)
        return dy[L]


print(DFS(N))
