# 동적 계획법
# 주어진 문제가 너무 복잡해서 한 번에 해결하기 힘들기 때문에,
# 문제의 속성만 유지한 채 크기만 작은 단위로 문제를 바꿔서 그 해를 구함.
# 크기를 조금 더 키운 문제의 해 vs 이전 해의 규칙을 구함. (bottom up 점화식)

import sys
sys.stdin = open('input.txt','r')

N = int(input())
dy = [0]*(N+1)

# initialize
dy[1] = 1 # 길이가 1인 선을 자르는 방법은 한가지
dy[2] = 2 # 길이가 2인 선을 자르는 방법은 두가지

for i in range(3, N+1) :
    dy[i] = dy[i-1] + dy[i-2]

print(dy[N])