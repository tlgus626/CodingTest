import sys
import collections

sys.stdin = open('input.txt', 'rt')

N, M = map(int, input().split())

sum = list()

for n in range(1,N+1) :
    for m in range(1,M+1) :
        sum.append(n+m)

cnt = collections.Counter(sum)

max_cnt = max(cnt.values())
max_sum = [k for k, v in cnt.items() if v == max_cnt]

# sorted : 순서대로 정렬하고, 정렬된 리스트 반환
print(sorted(max_sum))