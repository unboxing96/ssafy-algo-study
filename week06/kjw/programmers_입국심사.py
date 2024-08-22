'''
이진탐색 문제를 풀 땐 항상 정답으로 나오게 되는 값을 이진탐색 한다고 생각하기
'''
def solution(n, times):
    # if n <= len(times): 이렇게 하면 반례가 존재, 아예 빼버려도 아래코드로 돌아가는데 문제없음!
    #     result = times[n - 1]
    #     return result
    times.sort()
    start = 1
    end = times[-1] * n # 이렇게 될 수는 없겠지만 가장 시간 오래걸리는 면접관이 혼자 n명 다보는게 맥시멈값
    result = 0
    a = True    # while문 빠져나오기 위한 의미없는 변수
    while start <= end:
        possible_person = 0
        mid = (start + end) // 2
        for i in range(len(times)):
            possible_person += (mid // times[i])
            if possible_person >= n:    # mid시간동안 면접관들이 볼 수 있는 사람의 숫자 수
                result = mid    # 만약 다 볼 수 있다면 결과값 갱신하기
                end = mid - 1
                a = False
                break
        if not a:
            a = True
            continue
        else:
            start = mid + 1
    return result