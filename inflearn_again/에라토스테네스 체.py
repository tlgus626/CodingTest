N = 20

# 에라토스테네스 체
# 1. 2는 소수이므로 2의 배수를 모두 지운다.
# 2. 남아있는 수 가운데 3이 소수이므로 3의 배수를 모두 지운다.
# 3. 남아있는 수 가운데 5가 소수이므로 5의 배수를 모두 지운다.
# 4. repeat

ch = [0] * (N + 1)
cnt = 0

for i in range(2, N + 1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, N + 1, i):
            ch[j] = 1

print(cnt)
