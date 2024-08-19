import sys
sys.stdin = open('input.txt')

"""
1. 배열 안에, N ~ N+1 이하의 자연수만 들어있음.
2. 실패율:
2-1 스테이지에 도달했으나, 아직 클리어 하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수
3. (stages_len - stages_len2) : stages_len2는 이전의 도달한 플레이어의 수를 더한 값들 저장.
"""

N = int(input()) # 스테이지의 개수
stages = [2, 1, 2, 6, 2, 4, 3, 3]	# 게임을 이용하는 사용자가 멈춰있는 스테이지의 번호가 담긴 배ㅕㄹ
# [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages):

    result = [] # 출력할 결과값.
    check_stages = sorted(list(set(stages))) #{1, 2, 3, 4, 6} #[1, 2, 3, 4, 6] # 중간에 빈 스테이지를 찾기위함.
    stages_len = len(stages)
    stages_len2 = 0

    for i in range(1, N+1): # 1부터 N + 1까지 진행하면됨.
        if i in check_stages: # 만약 1~6의값이 순서대로 진행하는데, 하나의 값이 i안에 있으면
            result.append([i, (stages.count(i) / (stages_len - stages_len2))])
            # cnt = 1 / 8 / len2 =  0 > 1
            # cnt = 3 / 7  len2 = 1 > 4
            stages_len2 += stages.count(i)

            # result에 몇번째 스테이지인지, 해당 스테이지 클리어 못한 i의 수 / 도달한 플레이어 수(전제 스테이지 길이에서 이전 스테이지 길이 len을 빼면됨.)
        elif i not in check_stages: # 만약 1~6의값중 순서대로 진행하는데, 하나의 값이 없으면
            result.append([i, 0])

    answer = sorted(result, key = lambda x: (-x[1],x[0]))

    anwer_arr = []
    for i in range(len(answer)):
        anwer_arr.append(answer[i][0])

    return(anwer_arr)


print(solution(N,stages))
