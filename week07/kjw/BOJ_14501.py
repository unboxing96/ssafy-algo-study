# 문제해석 잘못해서 한참봄
n = int(input())
arr = [[0,0]]   # 인덱스 맞추려고
for i in range(n):
    arr.append(list(map(int, input().split())))
# dp는 n일째에 상담으로 얻을 수 있는 최대금액
dp = [0]*(n+1)
for i in range(1, n+1):
    if i+arr[i][0]-1 <= n:
        dp[i+arr[i][0]-1] = max(dp[i+arr[i][0]-1], dp[i-1]+arr[i][1])
    dp[i] = max(dp[i-1], dp[i])

print(dp[n])