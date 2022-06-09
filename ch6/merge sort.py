# merge sort : divide and conquer algorithm, 후위순회

# arr은 전역 리스트이므로, 함수 내에서 따로 정의할 필요 없음
def Dsort(lt, rt):
    if lt < rt:
        mid = (lt + rt) // 2
        Dsort(lt, mid)
        Dsort(mid + 1, rt)
        # 트리 다 나누고 나서 함수 본연의 일 시작
        ###########################################
        p1 = lt
        p2 = mid + 1
        tmp = []
        while p1 <= mid and p2 <= rt:
            if arr[p1] < arr[p2]:
                # 작은 값부터 넣어주기
                tmp.append(arr[p1])
                p1 += 1
            else:
                tmp.append(arr[p2])
                p2 += 1
        # 남은 원소들 넣어주기
        if p1 <= mid:  # 왼쪽 그룹에 원소가 남아있음
            tmp = tmp + arr[p1:mid + 1]
        if p2 <= rt:  # 오른쪽 그룹에 원소가 남아있음
            tmp = tmp + arr[p2:rt + 1]
        # tmp를 arr에 복사 (arr의 위치(=lt+i)에 맞춰서 복사해야 함!!)
        for i in range(len(tmp)):
            arr[lt + i] = tmp[i]
        ###########################################


if __name__ == '__main__':
    arr = [23, 11, 45, 36, 15, 67, 33, 21]
    print('Before sort : ', end='')
    print(arr)
    Dsort(0, 7)
    print('After sort : ', end='')
    print(arr)
