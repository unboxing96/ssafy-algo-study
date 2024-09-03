n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 삼각형 맨 마지막 줄 부터 역순으로 올라가기
for i in range(n-2, -1, -1):
    for j in range(len(arr[i])):
        if arr[i+1][j] > arr[i+1][j+1]:
            arr[i][j] += arr[i+1][j]
        else:
            arr[i][j] += arr[i+1][j+1]

print(arr[0][0])