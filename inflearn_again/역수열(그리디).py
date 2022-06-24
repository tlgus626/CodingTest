N = 8
R = [5, 3, 4, 0, 2, 1, 1, 0]

A = [0] * N

for i in range(N):
    for j in range(N):
        if R[i] == 0 and A[j] == 0:
            A[j] = i + 1
            break
        elif A[j] == 0:  # 빈자리 발견
            R[i] -= 1

for a in A:
    print(a, end=' ')