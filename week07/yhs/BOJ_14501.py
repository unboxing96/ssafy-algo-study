n = int(input())

dp = [0 for _ in range(n+1)]

for day in range(1, n+1):
    t, p = map(int, input().split())    # t: 상담기간, p: 페이
    if day + t - 1 <= n:                # 상담기간이 퇴사일을 넘지 않을 때
        dp[day+t-1] = max(max(dp[:day]) + p, dp[day+t-1])       # 전날까지 받을 수 있는 금액의 최댓값 + 오늘 상담일정으로 받을 수 있는 금액과
                                                                # 원래 dp 테이블의 값을 비교
print(max(dp))