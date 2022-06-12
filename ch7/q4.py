# 동적계획법 : 테이블 dy를 이용할 줄 알아야 해!!!
# topdown : 재귀(DFS)
# 메모이제이션 : 불필요한 재귀 호출 방지

import sys
sys.stdin = open('input.txt','r')

def DFS(len) :
    # cut
    if dy[len] > 0 :
        return dy[len]
    # 초깃값까지 좁혀졌을 때
    if len == 1 or len == 2 :
        return len
    else :
        # 계단을 오르는 방법은 하나 남기고 나머지 or 두개 남기고 나머지
        dy[len] = DFS(len-1) + DFS(len-2)
        return dy[len]

if __name__ == '__main__' :
    N = int(input())
    dy = [0]*(N+2)
    print(DFS(N+1))