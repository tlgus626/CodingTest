# 재귀함수를 이용한 깊이우선탐색

# DFS : 루트 노드에서 왼쪽 자식 노드로 뻗음. 갈 곳이 없으면 back -> 오른쪽 자식 노드 -> back -> 반복

# 전위순회 : 부 - 왼 - 오 순서 출력
def DFS(v) :
    if v > 7 :
        return
    else :
        print(v, end=' ') # 함수 본연의 일 : 다음 노드 호출 전에 내 일을 하는 것 = 전위순회
        DFS(v*2) # 왼쪽 노드 호출
        DFS(v*2+1) # 오른쪽 노드 호출

# # 중위순회 : 왼 - 부 - 오 순서 출력 (not popular)
# def DFS(v) :
#     if v > 7 :
#         return
#     else :
#         DFS(v*2) # 왼쪽 노드 호출
#         print(v, end=' ')  # 함수 본연의 일 : 왼쪽 노드 먼저 다 처리 = 중위순회
#         DFS(v*2+1) # 오른쪽 노드 호출
#
# # 후위순회 : 왼 - 오 - 부 순서 출력 (e.g., merge sort)
# def DFS(v) :
#     if v > 7 :
#         return
#     else :
#         DFS(v*2) # 왼쪽 노드 호출
#         DFS(v*2+1) # 오른쪽 노드 호출
#         print(v, end=' ')  # 함수 본연의 일 : 왼,오 노드 모두 먼저 처리 = 후위순회

if __name__ == '__main__' :
    DFS(1)