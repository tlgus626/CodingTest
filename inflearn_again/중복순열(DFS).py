N, M = 3, 2
cnt = 0
check = [0]*M

def DFS(v):
    global cnt
    if v == M:
        for i in range(M):
            print(check[i], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, N + 1):
            check[v] = i
            DFS(v + 1)


DFS(0)
print(cnt)
