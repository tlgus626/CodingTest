# 이분탐색 응용 버전.
# 결정 알고리즘 : 구하고자 하는 값의 범위를 알 수 있다.

import sys
sys.stdin = open('input.txt','rt')

K, N = map(int, input().split())

A = []

# 랜선의 길이는 1~802 (구하고자 하는 값은 기존 랜선의 최대 길이를 넘길 수 없음)
# K의 범위는 1~10000 -> 얼마나 큰 숫자일지 알 수 없으므로 함부로 sort 쓰면 안돼
MIN = 1
MAX = 0
for _ in range(K) :
    a = int(input())
    A.append(a)
    MAX = max(MAX, a)

result = 0

# MIN > MAX가 되는 순간 반복문 멈춤
while MIN <= MAX :
    MED = (MIN + MAX) // 2
    cnt = 0
    for a in A:
        cnt += a // MED
    if cnt >= N : # i.e., MED는 구하고자 하는 값보다 작거나 같음 (MIN<MED<200<MAX)
        # 결과값 변수에 저장
        result = MED
        # 187도 답이고 200도 답이야 : 더 좋은 답을 찾아야 해
        MIN = MED + 1
    elif cnt < N : # i.e., MED는 구하고자 하는 값보다 큼 (MIN<200<MED<MAX)
        MAX = MED - 1

print(result)