N, C = 5, 3
A = [1, 2, 8, 4, 9]
A.sort()

MIN = 1
MAX = A[N - 1]

result = 0

while MIN <= MAX:
    MED = (MIN + MAX) // 2

    cnt = 1
    end = A[0]
    for i in range(1, N):
        if A[i] - end >= MED:
            cnt += 1
            end = A[i]

    if cnt >= C:
        result = MED
        MIN = MED + 1
    else:
        MAX = MED - 1

print(result)
