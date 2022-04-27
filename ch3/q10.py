import sys
sys.stdin = open('input2.txt','r')

N = int(input())
R = list(map(int, input().split()))

A = [0]*N

# 오름차순 순서로 처리
# n번째 자료를 처리할땐 1~(n-1)번째 자료는 이미 자리 잡았으므로 신경쓰지 않아도 됨
for i in range(N) :
    for j in range(N) :
        # R[i] : i+1번째 앞에 놓인 i+1번째 수보다 큰 수는 R[i]개
        if R[i] == 0 and A[j] == 0 :
            A[j] = i+1
            break # 자기 자리 찾아 들어갔으니까 j 반복문은 필요 없음
        elif A[j] == 0 : # 빈자리 발견
            R[i] -= 1

for a in A :
    print(a, end=' ')