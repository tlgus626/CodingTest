import sys
sys.stdin = open('input2.txt','rt')

tot = list()

for i in range(2) :
    n = int(input())
    nums = list(map(int, input().split()))
    for j in range(n) :
        tot.append(nums[j])

# sort : nlogn
# but 각 리스트가 이미 정렬되어 있으므로 이를 이용해 8번 반복문만 돌면 복잡도는 n으로 감소
print(sorted(tot))