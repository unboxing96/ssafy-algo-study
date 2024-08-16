def solution(N, stages):
    count = [0 for _ in range(N)]                       # count[i] : i+1번째 스테이지 실패율
    answer = [x + 1 for x in range(N)]                  # [1, 2, 3, ... , n-1, n]
    users = len(stages)

    for i in range(N):
        if users == 0:                                  # 유저 수 0인 경우 : 실패율 0
            count[i] = 0
        else:
            count[i] = stages.count(i + 1) / users      # 실패율 계산
        users -= stages.count(i + 1)                    # 유저 수 갱신

    answer = sorted(answer, key=lambda x: count[x - 1], reverse=True)   # 실패율 순으로 정렬

    return answer