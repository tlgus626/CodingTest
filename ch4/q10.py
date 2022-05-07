import sys
import heapq
sys.stdin = open('input.txt','r')

# heap : root node, left child node & right child node
# 최소힙 : 부모 노드의 값이 자식 노드 값보다 무조건 작아야 함

heap = []

while True :
    x = int(input())
    if x == -1 :
        break
    elif x == 0 :
        if len(heap) == 0 :
            print(-1)
        else :
            print(heapq.heappop(heap))
    else :
        heapq.heappush(heap, x)