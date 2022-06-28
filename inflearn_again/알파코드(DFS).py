code = [2, 5, 1, 1, 4]
N = len(code)
code.insert(N, -1)
word = [0] * (N + 3)
cnt = 0


def DFS(L, P):
    global cnt
    if L == N:
        cnt += 1
        for j in range(P):
            print(chr(word[j] + 64), end='')
        print()
    else:
        for i in range(1, 27):
            if code[L] == i:
                word[P] = i
                DFS(L + 1, P + 1)
            elif i >= 10 and code[L] == i // 10 and code[L + 1] == i % 10:
                word[P] = i
                DFS(L + 2, P + 1)


DFS(0, 0)
print(cnt)
