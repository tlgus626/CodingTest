# 재귀함수 : 자기 자신을 불러오는 함수

# stack : last in first out
# (제일 마지막에 들어간 게 제일 먼저 나옴, 제일 처음 들어간 게 제일 나중에 나옴)
# 리스트로 pop, append 하면 stack 자료구조를 구현할 수 있음

# 재귀함수는 stack을 이용하여 작동됨
# 1) 결과값을 stack에 쌓아두고,
# 2) 조건에 해당하는 함수를 다 불러온 뒤,
# 3) first out : 위에서부터 결과값을 가져옴

import sys

sys.stdin = open('input.txt', 'r')


def DFS(x):
    if x == 0:
        # 이렇게만 해주면 함수를 종료함
        return
    else:
        DFS(x // 2)
        print(x % 2, end='')  # 재귀 다음에 print를 명령했으므로 top 값부터 출력 -> 거꾸로 출력됨


# 실행하면 여기로 옴
if __name__ == '__main__':
    n = int(input())
    DFS(n)
