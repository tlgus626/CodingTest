T = 20
K = 3
PN = [(5, 3), (10, 2), (1, 5)]
cnt = 0


def DFS(L, S):
    global cnt
    if S > T:
        return
    if L == K:
        if S == T:
            cnt += 1
    else:
        for i in range(PN[L][1] + 1):
            DFS(L + 1, S + PN[L][0] * i)


DFS(0, 0)
print(cnt)
