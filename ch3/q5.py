# greedy algorithm : '정렬'한 뒤에 차례대로 선택하면 됨

import sys
sys.stdin = open('input.txt','rt')

N = int(input())
A = []

for _ in range(N) :
    s, e = map(int, input().split())
    A.append((s,e)) # tuple

# 정렬 기준 : 끝나는 시간 기준으로 정렬
# (회의를 최대한 많이 해야하므로 시작 시간이 빠른 게 중요하지 않음. 하나의 회의가 빨리 끝나는 게 중요! e.g., 1시에 시작해서 7시에 시작할 수도 있음)
A.sort(key=lambda x : (x[1],x[0])) # 1순위는 끝시간 기준으로 정렬, 끝시간이 같다면 2순위 시작시간 기준으로 정렬

endtime = 0
cnt = 0

for s, e in A :
    if s >= endtime : # 이 회의 진행해
        endtime = e
        cnt += 1

print(cnt)