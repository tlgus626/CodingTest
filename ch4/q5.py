import sys
from collections import deque
sys.stdin = open('input.txt','r')

N, K = map(int, input().split())

# que : first in first out (입력은 뒷쪽, 출력은 앞쪽)
# in python : deque 자료구조 제공 (append/pop, appendleft/popleft)

deq = list(range(1,N+1))
deq = deque(deq)

while len(deq)>1 :
    for _ in range(K-1) :
        n = deq.popleft()
        deq.append(n)
    # k번째는 pop해서 왕자 제외
    deq.popleft()

print(deq[0])