import sys
sys.stdin = open('input.txt','rt')

cards = list(range(21))

# i가 필요 없음
for _ in range(10) :
    a, b = map(int, input().split())
    # 양 끝값을 바꾸기 위해서는 절반만 반복문 돌면 됨
    for i in range((b-a+1)//2) :
        # swap
        cards[a+i], cards[b-i] = cards[b-i], cards[a+i]

# 0th index's element 빼기
cards.pop(0)

# print는 list 형태가 아니라 value들만 나와야 함
for c in cards :
    print(c, end=' ')