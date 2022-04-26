import sys
sys.stdin = open('input.txt','r')

N, M = map(int, input().split())
A = list(map(int, input().split()))

# 가장 가벼운 사람 + 가장 무거운 사람이 같이 보트를 탈 수 있는지 확인 -> M을 넘으면 가장 무거운 사람 pop
# 가장 가벼운 사람 + (N-2)번째 사람이 같이 보트를 탈 수 있는지 확인 -> 타고갈 수 있으면 두 사람 pop
A.sort()

cnt = 0

# A가 비어있지 않으면 True, 비면 False = 반복문 끝
while A :
    # 마지막 한명 남으면 그냥 걔 보트 태워보내고 반복문 끝내기
    if len(A) == 1 :
        cnt += 1
        break
    # 두명 이상일 때 아래 if문 실행
    if A[0] + A[-1] > M :
        A.pop()
        cnt += 1
    else :
        A.pop(0)
        A.pop()
        cnt += 1

print(cnt)