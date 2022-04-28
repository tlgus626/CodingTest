import sys
sys.stdin = open('input.txt','r')

N, M = map(int, input().split())
N = [int(n) for n in str(N)]

# stack : last in first out
# (제일 마지막에 들어간 게 제일 먼저 나옴, 제일 처음 들어간 게 제일 나중에 나옴)
# 리스트로 pop, append 하면 stack 자료구조를 구현할 수 있음

stack = []

for n in N :
    # 만들어진 숫자는 최대한 커야함 : 직전에 들어간 값보다 크면 직전값은 필요없음
    while stack and M > 0 and stack[-1] < n :
        stack.pop()
        M -= 1
    # 가장 처음 while문에서는 stack==False이므로 바로 append
    # 작은 직전값들 다 빼고 내가 마지막 값으로 들어감
    stack.append(n)

# 원하는 자릿수(M)보다 더 큰 경우 sclicing 해야함
if M != 0 :
    stack = stack[:-M]

print(''.join(map(str, stack)))
# or
# for s in stack :
#     print(s, end='')