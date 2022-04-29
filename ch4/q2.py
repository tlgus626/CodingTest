import sys
sys.stdin = open('input.txt','r')

s = input()
stack = []
cnt = 0 # 쇠막대기 토막 수

for i in range(len(s)) :
    # 여는 괄호이면 stack에 쌓기
    if s[i] == '(' :
        stack.append(s[i])
    # 닫는 괄호이면 쇠막대기인지 레이저인지 확인해야 함
    else :
        # 레이저
        if s[i-1] == '(' :
            stack.pop()
            cnt += len(stack) # 쌓인 열린 괄호들 개수 (이 쇠막대기들은 다 절단되므로)
        # 쇠막대기의 끝
        else :
            stack.pop() # 해당 쇠막대기 시작 괄호 pop
            cnt += 1 # 절단 지점 이후의 쇠막대기 마지막 토막부분

print(cnt)