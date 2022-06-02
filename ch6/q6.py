import sys

sys.stdin = open('input.txt', 'r')


def DFS(L, P):
    global cnt
    if L == N:
        cnt += 1
        # 알파벳 출력
        for j in range(P):
            print(chr(word[j] + 64), end='')
        print()
    else:
        # 모든 알파벳에 대해 상태트리 뻗기
        for i in range(1, 27):
            # 한자리 숫자
            if code[L] == i:
                word[P] = i
                DFS(L + 1, P + 1)
            # 두자리 숫자
            elif i >= 10 and code[L] == i // 10 and code[L + 1] == i % 10:
                word[P] = i
                DFS(L + 2, P + 1)


if __name__ == '__main__':
    code = list(map(int, input()))  # [2, 5, 1, 1, 4]
    N = len(code)
    # 두자릿수 알파벳일 경우, 마지막 코드 확인할 때 index out of range error 발생하므로 마지막 자리에 -1을 채워주기
    code.insert(N, -1)
    word = [0] * (N + 3)
    cnt = 0
    DFS(0, 0)
    print(cnt)
