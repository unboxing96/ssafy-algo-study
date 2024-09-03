def solution(n):
    # dp_table 마지막 행의 각 열에 대해 dp 함수 호출
    for i in range(n):
        dp(n, i)

    return max(dp_table[n-1])


def dp(n, idx):
    global dp_table

    if not dp_table[n-1][idx]:
        if n == 1:          # 삼각형 맨 첫 번째 줄
            dp_table[n-1][idx] = triangle[0][0]
        elif n == 2:        # 삼각형 두 번째 줄
            dp_table[n-1][idx] = dp(1, 0) + triangle[n-1][idx]
        else:
            if idx == 0:    # n행의 첫 번쨰 열 : n-1행의 첫 번째 열에서 내려오는 것만 가능
                dp_table[n-1][idx] = dp(n-1, idx) + triangle[n-1][idx]
            elif idx == n-1:    # n행의 마지막 열 : n-1행의 마지막 열에서 내려오는 것만 가능
                dp_table[n-1][idx] = dp(n-1, idx-1) + triangle[n-1][idx]
            else:               # n행 i열 : n-1행 i열과 n-1행 i-1열에서 내려올 수 있음
                dp_table[n-1][idx] = max(dp(n-1, idx), dp(n-1, idx-1)) + triangle[n-1][idx]

    return dp_table[n-1][idx]


n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

dp_table = [[0 for j in range(1, i+2)] for i in range(n)]

print(solution(n))