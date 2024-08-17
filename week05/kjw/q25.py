# 예시코드 하나 만들어서 깃허브
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages):
    stages.sort()
    fail = []
    for i in range(1, N+1):
        try:
            a = stages.count(i)
            b = stages.index(i)
            c = len(stages[b:])
            fail.append((float(a/c), i))
        except:
            fail.append((0, i))

    fail.sort(key= lambda x: (-x[0], x[1]))

    answer = []
    for i in fail:
        answer.append(i[1])
    return answer

a = solution(N, stages)

print(a)