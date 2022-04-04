## 최솟값 구하기

arr = [5,3,7,9,2,5,2,6]

# arr[0] 으로 초기값을 정하고 1부터 반복문 돌려도 됨
arrMin = float('inf')

for i in range(len(arr)) :
    # 같은 값이 있을 때, 뒤쪽 걸 선택하라고 하면 <=로 해야겠지!
    if arr[i] < arrMin :
        arrMin = arr[i]

print(arrMin)