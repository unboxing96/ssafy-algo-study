T = int(input())
nums = []
for _ in range(T):
    nums.append(int(input()))

dp = [0 for i in range(max(nums)+1)]
dp[1], dp[2], dp[3] = 1, 2, 4           # 1: 1 / 2: 1+1 / 3: 1+1+1, 1+2, 2+1, 3
for i in range(4, len(dp)):
    dp[i] = sum(dp[i-3:i])              # dp[i-3]에 3 추가 / dp[i-2]에 2 추가 / dp[i-1]에 1 추가

for num in nums:
    print(dp[num])
