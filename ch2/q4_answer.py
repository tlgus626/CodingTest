import sys
sys.stdin = open('input2.txt','rt')

N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

# 각 리스트를 가리키는 pointer
p1 = p2 = 0
# 합친 리스트
c = list()

# 둘 중에 한 리스트를 처리하면 반복문 종료
while p1<N and p2<M :
    if a[p1] <= b[p2] :
        c.append(a[p1])
        p1 += 1
    else :
        c.append(b[p2])
        p2 += 1

# while 문이 끝나서 덜 append된 element들을 '+'로 추가
if p1<N :
    c = c + a[p1:]
if p2<M :
    c = c + b[p2:]

for x in c :
    print(x, end=' ')