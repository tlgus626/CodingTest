N, M = 9, 3
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]

MIN = max(A)
MAX = sum(A)

result = 0

while MIN <= MAX:
    MED = (MIN + MAX) // 2
    cnt = 1
    dvd = 0
    for a in A:
        if dvd + a > MED:  # 하나의 DVD 용량 초과
            cnt += 1
            dvd = a  # 새로운 DVD의 첫 번째 곡으로 a번째 곡 지정
        else:  # 하나의 DVD의 용량이 초과하지 않아서 a번째 곡 저장 가능
            dvd += a

    if cnt <= M:
        result = MED
        MAX = MED - 1
    elif cnt < N:
        MIN = MED + 1

print(result)
