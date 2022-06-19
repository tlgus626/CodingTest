N = 3
ints = [125, 15232, 97]


def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10  # 나머지
        x = x // 10  # 몫
    return sum


MAX = (0, 0)
for i in ints:
    DS = digit_sum(i)
    if MAX[1] < DS:
        MAX = (i, DS)
print(MAX[0])
