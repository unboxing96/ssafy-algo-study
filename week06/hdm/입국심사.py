import sys
sys.stdin = open('input.txt')


"""
N명이 입국심사.
입국심사를 기다리는사람 n, 한명심사시 걸리는시간 배열 times가 주어짐.

심사받는데 걸리는 시간의 최솟값 도출 더빨리 심사가 끝나는 쪽으로 이동할것임.
- 무조건 빠른순에 먼저갈것임.

6, [7,10] / 28분

# 1 2들어감.
0분에
# 3 4 들어감
7분 10분 = 10분경과
# 5 
7분 10분 = 10분경과

# 6
7분 
"""


def solution(n, times):

    answer = 0
    # 이진탐색은 무조건 정렬이 1회 필요함.
    times = sorted(times)
    # times를 정렬 한 후 가장 비효율적으로 검사하면? 10으로만검사 하면 화나겠찌?
    # 비효율적인 심사관한테만 검사받은 그값이 가장 오래걸리게 검사한 시간이 될것임.
    left, right = 1, (times[-1] * n)

    while left <= right: # 이진탐색 시작
        mid = (left+right) // 2
        poeple = 0 # 심사한 사람 수
        for time in times:
            # 각심사관이 mid분 동안 심사할 수 있는 살마으 ㅣ수
            poeple += (mid // time)
            if poeple >= n: #n명심사 가능하면 빠져나오기
                break
        if poeple >= n: #만약 people이 n명 이상이면
            answer = mid # 후보저장
            right = mid -1 # 더 작은 범위 1번더 체크 필요.
        # n 명이 되지 않으면,
        else:
            left = mid +1

    return answer


n = 6
times = [7,10]

print(solution(n,times))