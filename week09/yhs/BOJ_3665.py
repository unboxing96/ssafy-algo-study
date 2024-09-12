import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n = int(input())
    ranks = list(map(int, input().split()))

    m = int(input())
    indegree = [0] * (n)            # 작년 순위의 위상
    new_indegree = [0] * (n)        # 올해 순위의 위상

    for i in range(n):
        team = ranks[i]             # i+1위 팀
        indegree[team-1] = i
        new_indegree[team-1] = i

    for _ in range(m):
        a, b = map(int, input().split())
        if indegree[a-1] > indegree[b-1]:   # a팀의 순위가 b팀보다 낮을 경우
            new_indegree[a-1] -= 1
            new_indegree[b-1] += 1
        else:                               # a팀의 순위가 b팀보다 높을 경우
            new_indegree[a-1] += 1
            new_indegree[b-1] -= 1

    answer = [0] * n

    for i in range(n):
        if answer[new_indegree[i]]:         # 같은 위상인 팀이 존재할 경우 : IMPOSSIBLE
            print('IMPOSSIBLE')
            break
        answer[new_indegree[i]] = i+1       # 위상 순서대로 올해 순위 업데이트
    else:
        print(*answer)
