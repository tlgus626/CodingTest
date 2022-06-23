eq = '3+5*2/(7-2)'

stack = []
res = ''

for e in eq:
    if e.isdecimal():
        res += e
    else:
        if e == '(':
            stack.append(e)
        elif e == '*' or e == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(e)
        elif e == '+' or e == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(e)
        elif e == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            # 여는 괄호도 빼줘야 함
            stack.pop()

while stack:
    res += stack.pop()

print(res)
