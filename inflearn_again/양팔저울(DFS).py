N = 3
W = [1, 5, 7]
S = sum(W)
res = set()


def DFS(L, C):
    global res
    if C == N:
        if L > 0 and L <= S:
            res.add(L)
    else:
        DFS(L - W[C], C + 1)
        DFS(L + W[C], C + 1)
        DFS(L, C + 1)


DFS(0, 0)
print(S - len(res))
