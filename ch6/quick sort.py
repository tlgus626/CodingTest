# quick sort : divide and conquer algorithm, 전위순회

# arr은 전역 리스트이므로, 함수 내에서 따로 정의할 필요 없음
def Qsort(lt, rt):
    if lt < rt:
        pos = lt  # 분할된 영역의 시작 지점
        pivot = arr[rt]  # 파티션을 나눌 중심축
        for i in range(lt, rt):
            if arr[i] <= pivot:
                # swap
                arr[i], arr[pos] = arr[pos], arr[i]
                pos += 1
        # arr[rt], 즉 중심축이 중심으로 감!
        # arr[rt] 기준으로 왼쪽은 작은 값, 오른쪽은 큰 값으로 나뉨
        arr[rt], arr[pos] = arr[pos], arr[rt]
        # partition
        Qsort(lt, pos - 1)
        Qsort(pos + 1, rt)


if __name__ == '__main__':
    arr = [45, 21, 23, 36, 15, 67, 11, 60, 20, 33]
    print('Before sort : ', end='')
    print(arr)
    Qsort(0, 9)
    print('After sort : ', end='')
    print(arr)