import sys
sys.stdin = open('input.txt','rt')

A = [list(map(int, input().split())) for _ in range(7)]

cnt = 0

for i in range(7) :
    for j in range(3) :
        # row count
        a = A[i][j:(j + 5)]
        for k in range(5//2) :
            if a[k] != a[5-1-k] :
                break
        else :
            cnt += 1 # if a == a[::-1] : cnt += 1 도 가능
        # column count
        for l in range(5//2) :
            if A[j+l][i] != A[j+5-l-1][i] :
                break
        else :
            cnt += 1

print(cnt)