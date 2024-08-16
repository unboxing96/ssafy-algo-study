import sys
sys.stdin = open("02_18310_안테나.txt")

# 접근
# 거리의 합은 다음과 같이 구한다.
# pivot의 위치 이상의 값 a개 -> sum(a) - (a * pivot)
# pivot의 위치보다 작은 값 b개 -> (b * pivot) - sum(b)
# 거리의 합 -> sum(a) - sum(b) - (a - b) * pivot
# 이 값이 최소가 되는 pivot을 구하자.

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

# 구간합 (prefix sum) 계산
prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

min_distance = float('inf') # 1e9에서 무한으로 표현하니 정답
min_pivot = None

for i in range(n):
    pivot = arr[i]
    
    # pivot 보다 작은 쪽의 거리 합
    left_sum = pivot * i - prefix_sum[i]
    
    # pivot 보다 큰 쪽의 거리 합
    right_sum = (prefix_sum[n] - prefix_sum[i + 1]) - pivot * (n - i - 1)
    
    # 전체 거리 합
    total_distance = left_sum + right_sum
    
    if total_distance < min_distance:
        min_distance = total_distance
        min_pivot = pivot

print(min_pivot)
