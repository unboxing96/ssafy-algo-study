import sys
sys.stdin = open("01_2_123더하기.txt")

# 문제 분석
# case 1. -> 1
# 1

# case 2. -> 2
# 1 1
# 2

# case 3. -> 4
# 1 1 1
# 1 2
# 2 1
# 3

# case 4. -> 7
# 1 1 1 1
# 1 2 1
# 2 1 1
# 3 1
# 1 1 2
# 2 2
# 1 3


# case 5. -> 13
# 1 + 1 + 1 + 1 + 1
# 1 + 2 + 1 + 1
# 2 + 1 + 1 + 1
# 3 + 1 + 1
# 1 + 1 + 2 + 1
# 2 + 2 + 1
# 1 + 3 + 1
# 1 + 1 + 1 + 2
# 1 + 2 + 2
# 2 + 1 + 2
# 3 + 2
# 1 + 1 + 3
# 2 + 3

def get_123_composition(num):
    if dp[num]:
        return dp[num]
    
    if num == 1:
        dp[num] = 1
    elif num == 2:
        dp[num] = 2
    elif num == 3:
        dp[num] = 4
    else:
        dp[num] = get_123_composition(num - 1) + get_123_composition(num - 2) + get_123_composition(num - 3)
    
    return dp[num]


T = int(input())
for _ in range(T):
    n = int(input())
    dp = [0] * (n + 1)
    print(get_123_composition(n))
