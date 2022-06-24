N = 5
A = [[10, 13, 10, 12, 15], [12, 39, 30, 23, 11], [11, 25, 50, 53, 15], [19, 27, 29, 37, 27], [19, 13, 30, 13, 19]]
M = 3
B = [[2, 0, 3], [5, 1, 2], [3, 1, 4]]

for i in range(M):
    row, to, rot = B[i][0], B[i][1], B[i][2]
    if to == 0:
        for _ in range(rot):
            # 특정 행의 가장 첫 값을 pop해서 맨 뒤에 append
            A[row - 1].append(A[row - 1].pop(0))
    else:
        for _ in range(rot):
            # 특정 행의 가장 마지막 값을 pop해서 가장 앞에 append = insert(0)
            A[row - 1].insert(0, A[row - 1].pop())

cnt = 0
s = 0
e = N - 1

for i in range(N):
    for j in range(s, e + 1):
        cnt += A[i][j]
    if i < N // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(cnt)
