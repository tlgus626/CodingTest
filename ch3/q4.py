import sys
sys.stdin = open('input.txt','rt')

N, C = map(int, input().split())

A = [int(input()) for _ in range(N)]
A.sort() # 1,2,4,8,9 (수직선 상이므로 정렬 필요)

# 가장 가까운 두 말의 거리 범위 = 1~MAX(A)
MIN = 1
MAX = A[N-1]

result = 0

# MIN > MAX가 되는 순간 반복문 멈춤
while MIN <= MAX :
    # 가장 가까운 두 말의 거리 = 다른 말들의 거리는 모두 MED 보다 크거나 같아야 함
    MED = (MIN + MAX) // 2

    # 거리를 MED로 했을 때, 마구간에 최대 몇 마리의 말을 넣을 수 있는지?
    cnt = 1
    end = A[0]
    for i in range(1, N) : # i번째 말 배치해보자
        if A[i] - end >= MED :
            cnt += 1
            end = A[i]

    # C마리 이상 마구간에 넣을 수 있다면 답이 될 수 있음
    if cnt >= C :
        result = MED
        MIN = MED + 1
    else :
        MAX = MED - 1

print(result)
