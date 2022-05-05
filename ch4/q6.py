import sys
from collections import deque
sys.stdin = open('input.txt','r')

N, M = map(int, input().split())
deq = [(p,v) for p,v in enumerate(list(map(int, input().split())))]
deq = deque(deq)

cnt = 0

while deq :
    # any(n[1] < x[1] for x in deq) 이렇게 해도 됨
    (p,v) = deq.popleft()
    if any(v < d for _,d in deq) :
        deq.append((p,v))
    else :
        cnt += 1
        if p == M :
            break

print(cnt)