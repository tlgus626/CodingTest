import heapq

A = [5, 3, 6, 0, 5, 0, 2, 4, 0, -1]

heap = []

for a in A:
    if a == -1:
        break
    elif a == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -a)
