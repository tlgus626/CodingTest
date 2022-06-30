N, M = 4, 4
A = [[0, 1, 2, 0], [1, 0, 2, 1], [0, 2, 1, 2], [2, 0, 1, 2]]
house = []
pizza = []
for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            house.append((i, j))
        elif A[i][j] == 2:
            pizza.append((i, j))
combn = [0] * M
MIN = float('inf')


def DFS(L, S):
    global MIN
    if L == M:
        dist = 0
        for j in range(len(house)):
            hx = house[j][0]
            hy = house[j][1]
            hd = float('inf')
            for c in combn:
                px = pizza[c][0]
                py = pizza[c][1]
                hd = min(hd, abs(hx - px) + abs(hy - py))
            dist += hd
        if dist < MIN:
            MIN = dist
    else:
        for i in range(S, len(pizza)):
            combn[L] = i
            DFS(L + 1, i + 1)


DFS(0, 0)
print(MIN)
