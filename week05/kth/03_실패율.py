# 문제 분석
# 실패율: (실패자 / 도전자)
# 실패율의 내림차순으로 각 스테이지의 번호를 출력

# 접근
# stages 배열을 오름차순으로 정렬한다.
# current_stage = 1
# surviver_cnt = len(stages)
# 현재 스테이지 번호와 같은 값을 stages에서 찾는다. failure_cnt에 저장한다. 이들은 실패자이다.
    # 그 값을 surviver_cnt으로 나눈 것이 실패율이다.
    # (실패율, 스테이지 번호)를 failure_arr에 저장한다.
    # surviver_cnt에서 failure_cnt를 뺀다.
    # current_stage += 1

# 카운트 배열을 미리 생성하면 시간복잡도를 줄일 수 있을 것이다.
# 딕셔너리에 다음과 같이 저장하자. {스테이지 번호 : 카운트 수}


def solution(N, stages):
    answer = []
    surviver_cnt = len(stages)
    cnt_dict = {}
    failure_arr = []
    
    # 카운트 딕셔너리
    for stage in stages:
        cnt_dict[stage] = cnt_dict.get(stage, 0) + 1

    for current_stage in range(1, N + 1): # 스테이지 개수만큼 탐색
        if surviver_cnt > 0: # 생존자가 있는 경우에만 탐색
            failure_cnt = cnt_dict.get(current_stage, 0)
            failure_rate = failure_cnt / surviver_cnt
            failure_arr.append((failure_rate, current_stage))
            surviver_cnt -= failure_cnt
        else:
            failure_arr.append((0, current_stage)) # 생존자가 없으면 실패율은 0
    
    failure_arr.sort(key=lambda x : (-x[0], x[1])) # 조건에 맞춰 정렬
    
    for x in failure_arr:
        answer.append(x[1])
    
    return answer

N = 5
stages = [2, 4, 4, 4, 6]
result = solution(N, stages)
print(result)