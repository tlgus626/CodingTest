import sys
import heapq # 최소힙으로만 작동함
sys.stdin = open('input.txt','r')

heap = []

while True :
    x = int(input())
    if x == -1 :
        break
    elif x == 0 :
        if len(heap) == 0 :
            print(-1)
        else :
            print(-heapq.heappop(heap))
    else :
        heapq.heappush(heap, -x)