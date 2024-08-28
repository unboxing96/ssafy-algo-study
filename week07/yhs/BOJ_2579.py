# 단순 재귀 -> 시간 초과
# memoization 이용해야 한다

def dp(n):
    global dp_table

    if not dp_table[n]:
        if n == 1:
            dp_table[1] = stairs[1]
        elif n == 2:
            dp_table[2] = stairs[1]+stairs[2]
        elif n == 3:
            dp_table[3] = max(stairs[1]+stairs[3], stairs[2]+stairs[3])
        else:
            dp_table[n] = max(dp(n-2), dp(n-3)+stairs[n-1]) + stairs[n]

    return dp_table[n]


N = int(input())
stairs = [0 for _ in range(N+1)]
for i in range(1, N+1):
    stairs[i] = int(input())

dp_table = [0 for _ in range(N+1)]
print(dp(N))
