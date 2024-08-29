n = int(input())
arr = list(map(int, input().split()))

# 히터위치로 이진탐색
start = 0
end = len(arr) - 1

# 잘 생각해보면 히터를 임의 위치로 놓았을 때 가장 녹는시간이 오래 걸리는 쪽으로 히터가 이동해야함
# 직관적인 생각이 좀 요구됨
def check(heater):
    idx_max_time = (0, 0)
    for idx, value in enumerate(arr):
        idx_max_time = max(idx_max_time, (idx, abs(heater-idx)*value), key=lambda x: x[1])
    if idx_max_time[0] > heater:
        return True, idx_max_time[1]
    else:
        return False, idx_max_time[1]

result = float('inf')

while start <= end:
    mid = (start + end) // 2
    boolean, value = check(mid)
    if boolean:
        result = min(result, value)
        start = mid + 1
    else:
        result = min(result, value)
        end = mid - 1

print(result)