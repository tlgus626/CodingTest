# BFS : 큐 구조로 구현 (first in first out)
# FIFO : 들어간 순서대로 탐색하니까, 레벨 별로 탐색이 가능함!

import sys
from collections import deque

sys.stdin = open('input.txt','r')

MAX = 10000 # 좌표의 maximum value
check = [0]*(MAX+1)
coord = [0]*(MAX+1)

S, E = map(int, input().split())

dQ = deque()
dQ.append(S) # 현수 자리에서 시작

# initalize
check[S] = 1
coord[S] = 0

# dQ가 비어있기 전까지 반복
while dQ :
    # 큐의 first element : 현수의 현재 위치
    now = dQ.popleft()
    # 도착점을 발견하면 더 이상 탐색할 필요 없음
    if now == E :
        break
    # 다음 스텝은 세 가지 경우 중 하나
    for next in(now-1, now+1, now+5) :
        # 다음 스텝은 수직선 범위 내에 있어야 함
        if 0 < next <= MAX :
            # 다음 스텝은 한번이라도 들른 적 없어야 함
            if check[next] == 0 :
                dQ.append(next)
                check[next] = 1
                coord[next] = coord[now] + 1

print(coord[E])