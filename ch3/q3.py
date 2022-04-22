import sys
sys.stdin = open('input.txt','rt')

N, M = map(int, input().split())
A = list(map(int, input().split()))

# 최소 용량이 가질 수 있는 범위 : MAX(A) ~ SUM(A)
MIN = max(A) # DVD 한 장의 용량은 최소 MAX(A) 여야 함
MAX = sum(A) # DVD 한 장에 모든 노래 다 담으면 M개의 DVD를 만들 수 있으니까!

result = 0

# MIN > MAX가 되는 순간 반복문 멈춤
while MIN <= MAX :
    # DVD 한 장의 용량이 MED
    MED = (MIN + MAX) // 2

    # 용량이 MED인 DVD M장으로 N곡이 나뉠 수 있는지 확인
    cnt = 1
    dvd = 0
    for a in A :
        if dvd + a > MED : # 하나의 DVD 용량 초과
            cnt += 1
            dvd = a # 새로운 DVD의 첫 번째 곡으로 a번째 곡 지정
        else : # 하나의 DVD의 용량이 초과하지 않아서 a번째 곡 저장 가능
            dvd += a

    if cnt <= M : # i.e., MED는 구하고자 하는 값보다 작거나 같음 (MIN<17<MED<MAX)
        # 결과값 변수에 저장
        result = MED
        # 더 좋은 답을 찾아야 해
        MAX = MED - 1
    elif cnt < N : # i.e., MED는 구하고자 하는 값보다 큼 (MIN<MED<17<MAX)
        MIN = MED + 1

print(result)