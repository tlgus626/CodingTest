import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
bricks = []
for _ in range(N):
    a, h, w = map(int, input().split())
    bricks.append((a, h, w))

# sort descending by area
bricks.sort(reverse=True)

# dynamic list : max height
dy = [0] * N

# initialize
dy[0] = bricks[0][1]

# dynamic programming
MAX = 0

for i in range(1, N):
    m = 0
    for j in range(i):
        # 밑면의 조건은 무조건 만족 하므로 무게 조건만 만족 하면 쌓을 수 있음
        if bricks[i][2] < bricks[j][2] and dy[j] > m:
            m = dy[j]
    dy[i] = m + bricks[i][1]
    if dy[i] > MAX:
        MAX = dy[i]

print(MAX)