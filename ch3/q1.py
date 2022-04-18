import sys
sys.stdin = open('input.txt','rt')

N, M = map(int, input().split())

A = list(map(int, input().split()))
A.sort()

# 이분 검색
# 처음 선택한 중앙값이 만약 찾는 값보다 크면 그 값은 새로운 최댓값이 되며, 작으면 그 값은 새로운 최솟값이 된다.
# 검색 원리상 정렬된 리스트에만 사용할 수 있다는 단점이 있지만, 검색이 반복될 때마다 목표값을 찾을 확률은 두 배가 되므로 속도가 빠르다는 장점이 있다.

MIN = 0
MAX = N-1 # 0번 인덱스부터 자료가 들어가 있으므로!

# MIN > MAX가 되는 순간 반복문 멈춤
while MIN <= MAX :
    MED = (MIN+MAX)//2
    if A[MED] == M :
        print(MED+1)
        break
    elif A[MED] > M :
        MAX = MED - 1
    else :
        MIN = MED + 1