n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(k+1)

for i in range(n):
    w, v = arr[i][0], arr[i][1]
    for j in range(k, w-1, -1):
        dp[j] = max(dp[j], dp[j-w] + v)     # k-w만큼 가방에 담아놓고 w만큼 더담으면 그게 더 크니? 하고 생각

print(max(dp))