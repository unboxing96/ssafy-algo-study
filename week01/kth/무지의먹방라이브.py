# 문제 분석
# 네트워크 장애 후 재개...는 그냥 말을 꼬아놓은 것이고, 
# 그냥 k초가 되었을 때 먹어야 할 음식의 번호를 return 하면 된다.
# 더 이상 섭취할 음식이 없다면 -1을 return

# food_times의 원소가 1억 이상이고, k는 2 * 10^13 이상이다. 과하게 크다.
# 문제에서 주어진 대로 원형큐를 순회하듯 문제를 풀면 시간 초과가 발생할 것이다.
# 나눗셈을 활용해서 뭉탱이로 원소 값을 줄여서 계산해야 한다.
# 그런데 이게 왜 그리디인지는 ... 모르겠다. 기억이 안 난다.

# 0초부터 먹기 시작하므로, k + 1번째의 위치라고 생각하는 쪽이 편하다.

# 접근
# 예시 테스트 케이스: [4, 1, 3, 3, 4]
# -> 12: [4, 1, 3, 3, 4]
# -> 7: [3, 0, 2, 2, 3]
# -> 3: [2, 0, 1, 1, 2]
# -> 0: [1, 0, 0, 0, "2"]
# 위 배열로 counter를 만든다. -> [0, 1, 0, 2, 2]
# 각 인덱스는 그릇에 있는 음식의 양을 의미한다.

def solution(food_times, k):
    foods = [(time, idx) for idx, time in enumerate(food_times)]
    foods.sort() # 시간을 기준으로 오름차순 정렬
    
    n = len(food_times)
    prev_time = 0 # 최근에 하나의 레벨을 제거한 시간
    for i, (time, idx) in enumerate(foods):
        diff = time - prev_time
        if diff != 0: # 다른 레벨이라면
            total_eat_time = diff * n # 현재 레벨에서 한 바퀴 돌리기 위해 드는 시간 * 현재 레벨의 개수
            if total_eat_time <= k: # k 시간 안에 
                k -= total_eat_time
                prev_time = time
            else:
                k %= n # 마지막 탐색 레벨. 다 돌고 나머지
                remaining_foods = sorted(foods[i:], key = lambda x : x[1]) # 현재 레벨 이후에서, idx를 기준으로 정렬
                return remaining_foods[k][1] + 1 # 나머지번째의 idx + 1 # +1은 정답 포맷 맞추기 위함
    
        n -= 1

    return -1  # 더 이상 먹을 음식이 없으면 -1 반환

print(solution([3, 1, 2], 5))  # 예시 테스트 케이스
