import sys

sys.stdin = open('input.txt', 'rt')

N, M = map(int, input().split())

cnt = [0]*(N+M+3) # 일부러 넉넉히

for n in range(1,N+1) :
    for m in range(1,M+1) :
        cnt[n+m] += 1

cnt_max = 0

for c in range(n+m+1) :
    if cnt[c] > cnt_max :
        cnt_max = cnt[c]

# cnt_max에 해당하는 sum을 출력해야 함
for c in range(n+m+1) :
    if cnt[c] == cnt_max :
        print(c, end=' ')