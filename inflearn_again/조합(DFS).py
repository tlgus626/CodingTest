N, M = 5, 3
result = [0]*(N+1)
cnt = 0


def DFS(L, S):
    global cnt
    if L == M:
        for j in range(M):
            print(result[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(S, N + 1):
            result[L] = i
            DFS(L+1, i+1)


DFS(0, 1)
print(cnt)