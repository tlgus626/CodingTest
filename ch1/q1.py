n, k = map(int, '6 3'.split())

cnt = 0

for i in range(1, n+1) :
    if n % i == 0 : # i가 n의 약수에 해당
        cnt += 1
    if cnt == k : # k번째 약수
        print(i)
        break # 반복문을 더 이상 돌릴 이유가 없음
else : # python : for ~ else
    print(-1) # 6의 5번째 약수 같은 건 없으니까 이럴 경우 -1 출력