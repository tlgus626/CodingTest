import sys
sys.stdin = open('input.txt','rt')

N = int(input())
A = []

for _ in range(N) :
    h, w = map(int, input().split())
    A.append((h,w)) # tuple

A.sort(reverse=True)

# 첫번째 사람은 키로 이겼으니까 무조건 선수 리스트에 포함됨
# 마찬가지로 n번째 사람은 n+1번째 이후 사람들을 신경 쓸 필요가 없음 (키로 이미 이겼으니까!)
# therefore, n번째 사람보다 위쪽(1~(n-1)번째)만 살펴서 몸무게만 이기면 선수 리스트에 포함
max_w = A[0][1]
cnt = 0

for _, w in A :
    if w > max_w :
        max_w = w
        cnt += 1

print(cnt)