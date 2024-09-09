import sys
sys.stdin = open('input.txt')

"""
상담원으로 일하는 백준이 퇴사
오늘부터 N + 1 일째 되는 날 퇴사하려함.
남은 N일동안 최대한 많은 상담하려함.



최대수익이 문제 조건임.
count가 존재한다면 = 1
1일에 벌어들이는 수익보다 2
조건:
1. cnt 가 N을 넘어서면 진행불가. 
2. 하루에 벌어들이는 최대수익을 체크해야됨.(그것을 진행해야됨)
2.1. p / t = 돈 나누기 T로 배열 따로 저장. 1일 ~ 7일 저장해두기.


"""
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)] #[[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]]

# 메모이제이션 준비
dp = [0] * (N+1)

for i in range(N):
    duration, profit = arr[i]

    # 만약 퇴사일 기간내라면, 상담을 진행했으면
    if i + duration <= N:
        # 상담이 끝난날은 = 상담이 끝나는 날까지 얻을 수 있는 최대 이익 / 현재 날짜에서 상담을 했을대 얻을 수 있는 이익 비교
        dp[i+duration] = max(dp[i+duration], dp[i] + profit)
    # 상담을 진행하지 않으면
        # dp[i]를 dp[i+1]로 옮겨주기= 현재까지의 이익과 /상담 진행하지 않았을대 이익 비교
    dp[i + 1] = max(dp[i+1], dp[i])

print(dp[N])

