N, M = 3, 2
check = [0] * (N + 1)
result = [0] * M
cnt = 0

def DFS(v):
    global cnt
    if v == M:
        for j in range(M):
            print(result[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, N + 1):
            if check[i] == 0:
                check[i] = 1
                result[v] = i
                DFS(v + 1)
                check[i] = 0

DFS(0)
print(cnt)