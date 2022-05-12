import sys

sys.stdin = open('input.txt', 'r')


# 상태트리 : 문제 해결 과정의 중간 상태를 각각 한 노드로 나타낸 트리
# 예 : 왼쪽 노드는 부분집합에 포함됨, 오른쪽 노드는 부분집합에 포함되지 않음

def DFS(v):
    if v == n + 1:
        # 종료지점에 도달함
        for i in range(1, n + 1):
            if check[i] == 1:
                print(i, end=' ')
        # 줄바꿈
        print()
    else:
        # 부분집합에 포함
        check[v] = 1
        DFS(v + 1)
        # 부분집합에 포함하지 않음
        check[v] = 0
        DFS(v + 1)


if __name__ == '__main__':
    n = int(input())
    check = [0] * (n + 1)  # 부분집합 포함 여부 체크
    DFS(1)
