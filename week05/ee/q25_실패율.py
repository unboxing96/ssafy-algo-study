def solution(N, stages):
    counts = [[0]*2 for _ in range(N+2)]

    for stage in stages:
        counts[stage][0] += 1 # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수
        for i in range(1, stage+1):
            counts[i][1] += 1 # 스테이지에 도달한 플레이어 수

    # 실패율
    per = [[0]*2 for _ in range(N)]
    for i in range(1, N+1):
        per[i-1][0] = i # 인덱스 저장
        if counts[i][1]:
            per[i-1][1] = counts[i][0] / counts[i][1] # 실패율율
       else:
            per[i-1][1] = 0 # 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.

    per.sort(key= lambda x: -x[1]) # 내림차순 정렬
    answer = [x[0] for x in per]

    return answer