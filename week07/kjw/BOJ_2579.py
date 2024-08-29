# 순간 생각 잘못해서 헤맸네요 ㅎㅎ;;
n = int(input())
arr = [int(input()) for _ in range(n)]

# dp에 각 계단까지 오는 최댓값 저장
dp = [0]*(n+1)
dp[1] = arr[0]
if n == 1:
    print(dp[1])
else:
    dp[2] = arr[0] + arr[1]
    if n == 2:
        print(dp[2])
    else:
        for i in range(3,n+1):
            dp[i] = max(dp[i-2]+arr[i-1], dp[i-3]+arr[i-2]+arr[i-1])
        print(dp[n])