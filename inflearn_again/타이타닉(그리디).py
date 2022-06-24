n, m = 5, 140
A = [90, 50, 70, 100, 60]
A.sort()

cnt = 0

while A:
    if len(A) == 1:
        cnt += 1
        break
    if A[0] + A[-1] > m:
        A.pop()
        cnt += 1
    else:
        A.pop(0)
        A.pop()
        cnt += 1

print(cnt)
