import sys
sys.stdin = open('input.txt','r')

eq = input()

res = ''
stack = []

for e in eq :
    # 숫자
    if e.isdecimal() :
        res += e
    # 연산자
    else :
        if e == '(' :
            stack.append(e)
        # 우선 순위가 같은 연산자만 stack에서 같이 꺼내올 수 있음 (열린 괄호도 제외되는 것!)
        elif e == '*' or e == '/' :
            while stack and (stack[-1] == '*' or stack[-1] == '/') :
                res += stack.pop()
            stack.append(e)
        # 자기보다 우선 순위가 무조건 빠르므로 (괄호 제외) 전부 stack에서 꺼내야 함
        elif e == '+' or e == '-' :
            while stack and stack[-1] != '(' :
                res += stack.pop()
            stack.append(e)
        elif e == ')' :
            while stack and stack[-1] != '(' :
                res += stack.pop()
            # 여는 괄호도 빼줘야 함
            stack.pop()

while stack :
    res += stack.pop()

print(res)