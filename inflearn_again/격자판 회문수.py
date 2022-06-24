A = [[2, 4, 1, 5, 3, 2, 6],
     [3, 5, 1, 8, 7, 1, 7],
     [8, 3, 2, 7, 1, 3, 8],
     [6, 1, 2, 3, 2, 1, 1],
     [1, 3, 1, 3, 5, 3, 2],
     [1, 1, 2, 5, 6, 5, 2],
     [1, 2, 2, 2, 2, 1, 5]]

cnt = 0

for i in range(7):
    for j in range(3):
        # row count
        a = A[i][j:(j + 5)]
        if a == a[::-1]:
            cnt += 1
        # column count
        for l in range(5 // 2):
            if A[j + l][i] != A[j + 5 - l - 1][i]:
                break
        else:
            cnt += 1

print(cnt)
