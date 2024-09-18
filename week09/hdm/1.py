import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    ti = list(map(int, input().split()))
    change_cnt = int(input())

    # 진입차수와 그래프 초기화
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]

    # 기존 순위 정보로 그래프 구축
    for i in range(n):
        for j in range(i + 1, n):
            graph[ti[i]].append(ti[j])
            indegree[ti[j]] += 1

    # 바뀐 순위 반영
    for _ in range(change_cnt):
        a, b = map(int, input().split())
        # a가 b보다 높아진 경우, 반대 방향으로 바꿔줌
        if b in graph[a]:
            graph[a].remove(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[b].remove(a)
            graph[a].append(b)
            indegree[b] += 1
            indegree[a] -= 1

    def topology_sort():
        result = []
        q = deque()

        # 진입차수가 0인 팀을 큐에 삽입
        for i in range(1, n+1):
            if indegree[i] == 0:
                q.append(i)

        while q:
            # 큐에 두 개 이상의 원소가 있다면 순서를 결정할 수 없음
            if len(q) > 1:
                return -1
            now = q.popleft()
            result.append(now)

            # 해당 팀과 연결된 다른 팀들의 진입차수 감소
            for next_team in graph[now]:
                indegree[next_team] -= 1
                if indegree[next_team] == 0:
                    q.append(next_team)

        # 모든 팀을 순서대로 정렬하지 못한 경우
        if len(result) != n:
            return 0

        return result

    result = topology_sort()

    if result == 0:
        print("?")
    elif result == -1:
        print("IMPOSSIBLE")
    else:
        print(" ".join(map(str, result)))
