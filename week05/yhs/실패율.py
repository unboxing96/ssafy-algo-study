def solution(N, stages):
    count = [0 for _ in range(N)]
    answer = [x + 1 for x in range(N)]                  # [1, 2, ... , N]
    users = len(stages)

    for i in range(N):
        if users == 0:                                  # 유저수가 0일 때 : 실패율 0
            count[i] = 0
        else:
            count[i] = stages.count(i + 1) / users      # count의 i번째 인덱스: i+1번째 스테이지의 실패율
        users -= stages.count(i + 1)                    # 유저 수 갱신

    answer = sorted(answer, key=lambda x: count[x - 1], reverse=True)   # 실패율순으로 정렬

    return answer
