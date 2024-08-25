# 문제 분석
# 소요 시간 m을 이분탐색하며 조건을 성립하는지 판단한다.
# times의 원소를 time이라고 할 때, m // time 값을 모두 더한 것이 처리한 사람 수이다.
# 처리한 사람의 수가 n명 이상이라면 m을 너무 크게 설정한 것이다. 범위를 줄인다.
    # 조건은 달성했으니 answer를 갱신한다.
# n 미만이라면 범위를 늘린다.

def solution(n, times):
    answer = 0
    
    start = min(times)
    end = max(times) * n
    
    while start <= end:
        m = (start + end) // 2
        tmp_sum = 0
        for time in times:
            tmp_sum += m // time
            
        if tmp_sum >= n:
            end = m - 1
        else:
            start = m + 1
    
    return start