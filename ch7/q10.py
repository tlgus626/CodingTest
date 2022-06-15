import sys

sys.stdin = open('input.txt', 'r')

N, L = map(int, input().split())

# dynamic table dy[j] = 가방에 'j'g까지 담을 수 있을 때, 얻을 수 있는 최대 가치
# e.g., dy[6] : 5g짜리 보석을 넣을 수도 있고, 3g짜리 보석을 두개 넣을 수도 있음.
# 3g까리 보석 두개 넣기 = dy[3] + value of 3g
dy = [0] * (L + 1)

# dynamic programming
for _ in range(N):
    w, v = map(int, input().split())
    # 'w'g부터 담을 수 있음
    for j in range(w, L + 1):
        # dy[j-w] : w'g' 보석을 담는다고 가정했을 때, 최대 가치
        dy[j] = max(dy[j], dy[j - w] + v)

print(dy)
