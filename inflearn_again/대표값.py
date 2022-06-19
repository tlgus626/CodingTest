N = 10
score = [45, 73, 66, 87, 92, 67, 75, 79, 75, 80]

# round digit 지정 안하면 int 형식으로 출력
# round : round_half_even 방식 : 정확히 4, 5 사이의 간격이 같으면 짝수인 4 반환
# solution : 0.5 더하고 floor function(int()도 floor)

avg = sum(score) / N
avg = avg + 0.5
avg = int(avg)

min = float('inf')

for idx, s in enumerate(score):
    diff = abs(s - avg)
    if diff < min:
        min = diff
        min_s = s
        min_i = idx + 1
    elif diff == min:
        if s > min_s:  # 75, 75가 만나도 이 if문은 작동하지 않음(idx는 빠른 번호로 유지)
            min_s = s
            min_i = idx + 1

print(avg, min_i)
