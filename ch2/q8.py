import sys
sys.stdin = open('input2.txt','rt')

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())

for i in range(M) :
    row, to, rot = map(int, input().split())
    # left rotation
    if to==0 :
        for _ in range(rot) :
            # row=2라고 하면 실제 두번째 행은 -1
            # 특정 행의 가장 첫 값을 pop해서 맨 뒤에 append
            A[row-1].append(A[row-1].pop(0))
    # right rotation
    else :
        for _ in range(rot) :
            # 특정 행의 가장 마지막 값을 pop해서 가장 앞에 append = insert(0)
            # pop의 default는 가장 마지막 값
            A[row-1].insert(0, A[row-1].pop())

# cnt
cnt = 0
s = 0
e = N-1

for i in range(N) :
    for j in range(s, e+1) :
        cnt += A[i][j]
    if i < N//2 :
        s += 1
        e -= 1
    else :
        s -= 1
        e += 1

print(cnt)