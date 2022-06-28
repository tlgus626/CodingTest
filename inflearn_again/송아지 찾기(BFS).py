from collections import deque

S, E = 5, 14

MAX = 10000  # 좌표의 maximum value
check = [0] * (MAX + 1)
coord = [0] * (MAX + 1)

dQ = deque()
dQ.append(S)

check[S] = 1

while dQ:
    now = dQ.popleft()
    if now == E:
        break
    for next in (now - 1, now + 1, now + 5):
        if 0 < next <= MAX:
            if check[next] == 0:
                dQ.append(next)
                check[next] = 1
                coord[next] = coord[now] + 1

print(coord[E])
