import sys
sys.stdin = open('input.txt','rt')

string = input()

num = 0

for s in string : # string을 일일이 슬라이싱하지 않아도 돼!
    if s.isdecimal() : # isdigit은 문자가 아닌 모든 숫자, isdecimal은 0~9
        num = num*10 + int(s) # 이거 기억해!!

cnt = 0

for i in range(1, num+1) :
    if num % i == 0 :
        cnt += 1

print(num, cnt, sep='\n')